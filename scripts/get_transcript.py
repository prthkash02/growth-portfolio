#!/usr/bin/env python3
"""
get_transcript.py — pull a YouTube transcript into a clean Markdown file.

Used to collect talks/interviews from the experts in research/sources.md
(e.g. Kyle Coleman's AI-prospecting talk, Becc Holland's Flip the Script
sessions) into research/youtube-transcripts/.

Usage:
    python scripts/get_transcript.py <VIDEO_URL_OR_ID> "<Author>" "<Title>"

Example:
    python scripts/get_transcript.py \
        https://www.youtube.com/watch?v=7OdRu6_YqGc \
        "Kyle Coleman" "How to Use AI for Prospecting Executives"

Output:
    research/youtube-transcripts/<author-slug>/<title-slug>.md

Setup:
    pip install youtube-transcript-api
Fallback if captions are disabled:
    yt-dlp --write-auto-sub --skip-download --sub-lang en <url>
"""

import re
import sys
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    sys.exit("Missing dependency. Run: pip install youtube-transcript-api")

OUT_ROOT = Path(__file__).resolve().parent.parent / "research" / "youtube-transcripts"


def video_id(url_or_id: str) -> str:
    """Accept a full URL or a bare 11-char video id."""
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", url_or_id)
    return m.group(1) if m else url_or_id


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit('Usage: python scripts/get_transcript.py <URL_OR_ID> "<Author>" "<Title>"')

    raw, author, title = sys.argv[1], sys.argv[2], sys.argv[3]
    vid = video_id(raw)

    try:
        fetched = YouTubeTranscriptApi().fetch(vid)
    except Exception as e:  # transcript disabled, no captions, etc.
        sys.exit(f"Could not fetch transcript for {vid}: {e}\n"
                 f"Fallback: yt-dlp --write-auto-sub --skip-download {raw}")

    snippets = list(fetched)
    body = "\n".join(s.text.strip() for s in snippets if s.text.strip())

    out_dir = OUT_ROOT / slug(author)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug(title)}.md"

    header = (
        f"# {title}\n\n"
        f"- **Author:** {author}\n"
        f"- **Source:** https://www.youtube.com/watch?v={vid}\n"
        f"- **Collected via:** youtube-transcript-api\n\n"
        f"---\n\n"
    )
    out_path.write_text(header + body + "\n", encoding="utf-8")
    print(f"Saved {len(snippets)} lines -> {out_path.relative_to(OUT_ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
