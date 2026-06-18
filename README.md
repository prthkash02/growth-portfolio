# growth-portfolio
Growth marketing portfolio project: AI tools, research, outreach, and campaign workflows.

# Growth Marketing Portfolio

## About This Project
A portfolio project demonstrating AI tool setup, developer workflow, and technical problem-solving ability.

---

## Tools Installed

- **Cursor IDE**: AI-powered code editor (cursor.com)
- **Claude Code** (Cursor extension): AI coding assistant by Anthropic, 
  authenticated via claude.ai account
- **Codex** (Cursor extension): AI coding agent by OpenAI, installed manually after extension panel installation failed

---

## Steps Completed

1. Downloaded and installed Cursor IDE on macOS (Apple Silicon)
2. Installed the Claude Code extension from Cursor's Extensions panel and authenticated with my Claude.ai account
3. Installed the Codex extension from Cursor's Extensions panel and authenticated with my ChatGPT account
3. Created a public GitHub repository
4. Opened the repository in Cursor
5. Created this README documenting tools, steps, and issues encountered

---

## Issues Encountered & How I Solved Them

### Codex Extension
- Searched for "Codex" in Cursor's Extensions panel
- Found "Codex, OpenAI's coding agent" but installation failed with the error:
  *"Error while installing 'Codex – OpenAI's coding agent' extension."*
- Resolved by running the manual install script from OpenAI's website via terminal, after which the extension became functional

### Claude Code Sign In
- Claude Code extension did not automatically open browser for authentication
- Resolved by manually triggering sign in via `Ctrl+Shift+P` → 
  "Claude Code: Sign In"
---

## Notes
I approach problems the way I'd approach any growth challenge, figure out what's needed, try to solve it, document what happened, and flag blockers clearly rather than guessing blindly.

---

# Step 2 — Research Project

**Topic: Cold outreach pipeline for B2B SaaS (through an AI-native lens).**

## Why this topic
I come from a sales background, so I can actually *judge* outreach advice instead of just summarizing it — which is the point of this exercise. I framed it around AI ("how is AI changing cold outreach?") to match the AI-native nature of the role, while staying on ground where I can tell a strong tactic from a loud one.

## What's in `/research`
- [`sources.md`](research/sources.md) — the 10 experts, each with proof, links, and why they're high-signal, plus the core tension I set out to resolve.
- [`youtube-transcripts/`](research/youtube-transcripts) — full talk/interview transcripts (pulled via API).
- [`linkedin-posts/`](research/linkedin-posts) — recent posts, organized per author.
- [`other/newsletters/`](research/other/newsletters) — newsletter/framework material.
- [`other/fact-check.md`](research/other/fact-check.md) — independent verification of 10 specific claims.
- [`synthesis.md`](research/synthesis.md) — my point of view tying it all together (the seed of a real playbook).

## The 10 experts (and the one-line reason)
1. **Josh Braun** — anti-pushy "poke the bear" outreach; the human-relevance anchor.
2. **Jason Bay** (Outbound Squad) — repeatable cold-call frameworks, trained 20k+ reps.
3. **Will Allred** (Lavender) — data-backed cold email; built on 2B+ analyzed emails.
4. **Jed Mahrle** (Practical Prospecting) — bridges human craft and automation.
5. **Leslie Venetz** — omnichannel outbound; USA Today bestselling author.
6. **Nick Cegelski** (30MPC) — #1 sales podcast; *Cold Calling Sucks*, backed by 300M+ calls.
7. **Florin Tatulea** — GTM engineering: actually *builds* AI-agent outbound systems.
8. **Kyle Coleman** (ex-Copy.ai) — best on AI research + personalization at scale.
9. **Thibaut Souyris** — creative outreach (video/voice) AI can't fully replicate.
10. **Becc Holland** (Flip the Script) — personalization (1:1) vs. relevance (1:many) — the key idea.

## What I collected
- **6 talk/interview transcripts** — Kyle Coleman, Jason Bay (~2,800 lines), Josh Braun (x2), Becc Holland (x2).
- **~22 LinkedIn posts across 8 authors** — Leslie Venetz, Will Allred, Jed Mahrle, Thibaut Souyris, Josh Braun, Jason Bay, Nick Cegelski, Florin Tatulea (organized one file per author).
- **Newsletter / framework material** — the full 30MPC cold-calling framework + Florin Tatulea's *Prospecting from the Trenches* summaries and podcast.
- **10 fact-checked claims** (`other/fact-check.md`) + **a synthesis POV** (`synthesis.md`).

**Coverage:** all 10 experts have at least one collected artifact; most have two or more (e.g. transcript + LinkedIn, or framework + LinkedIn).

## Tools & methods
- **`scripts/get_transcript.py`** — I wrote a small Python tool (using `youtube-transcript-api`) to pull YouTube transcripts into clean, headed Markdown, organized by author.
- Public newsletters/frameworks collected via direct fetch; paywalled Substacks captured as public summaries (and supplemented with the author's LinkedIn).
- Claims verified against independent primary sources (acquisition announcements, retailers, company sites).

## Issues I ran into & how I solved them
- **`youtube-transcript-api` changed its API in v1.x** — the old `.get_transcript()` static method was gone. I read the installed version's surface, found it now uses an instance method (`YouTubeTranscriptApi().fetch()`), and updated the script.
- **Paywalled newsletters** (Jed Mahrle, Florin Tatulea Substacks) — only previews are public. Rather than fake completeness, I saved the public summaries and noted the paywall, then leaned on their LinkedIn for the substantive content.
- **LinkedIn is login-walled** — scraping breaks against their ToS and is unreliable, so I collected those posts manually and documented that choice (judgment over a brittle hack).

## What I'd build next
The [synthesis](research/synthesis.md) lays out the thesis: **AI handles relevance at scale; humans win on true 1:1 personalization for high-value accounts.** That tiered model is the spine of the cold-outreach playbook this research is meant to support.
