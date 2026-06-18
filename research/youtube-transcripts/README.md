# YouTube Transcripts

Transcripts pulled from the experts' videos/talks, organized one folder per author, one file per video.

Collection method: `youtube-transcript-api` (Python) via [`scripts/get_transcript.py`](../../scripts/get_transcript.py), falling back to `yt-dlp --write-auto-sub` where captions are disabled. Each file keeps the video title, source URL, and collection method at the top.

Collected: Kyle Coleman, Jason Bay, Josh Braun (x2), Becc Holland (x2).
