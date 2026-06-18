# Growth Marketing Portfolio

A portfolio project for the 100Hires Junior Growth Marketing role. It has two parts:

- **Step 2, a research project** on cold outreach for B2B SaaS. This is the main work.
- **Step 1, the AI-tool setup** that got the environment ready.

---

## Step 2: Cold Outreach for B2B SaaS

Ten genuinely strong practitioners, their recent content collected and organised, annotated with enough judgment to seed a real outbound playbook later.

### Why this topic
I come from a sales background, so I can actually judge whether outreach advice is good or just loud, instead of just summarising it. I framed the topic around AI ("where is AI genuinely changing cold outreach, and where is it just adding noise?") to fit the AI-native nature of the role, while staying on ground where I can tell a strong tactic from a loud one.

### What's in the repo

```
research/
  sources.md            The 10 experts: links, dates, annotations, and the index
  synthesis.md          My point of view + a playbook skeleton built from it
  linkedin-posts/       Posts organised by author (9 files)
  youtube-transcripts/  Transcripts organised by author and video (6 transcripts)
  other/
    fact-check.md       10 specific claims verified against independent sources
    newsletters/        30MPC cold-calling framework + Florin Tatulea summaries
scripts/
  get_transcript.py     The YouTube transcript fetcher I wrote
  requirements.txt
```

### The 10 experts
Full annotations, links, and content dates are in [`research/sources.md`](research/sources.md). In short:

1. **Josh Braun** : "poke the bear", anti-pushy outreach. The human-relevance anchor.
2. **Jason Bay** (Outbound Squad) : repeatable cold-call frameworks; trained 20k+ reps.
3. **Will Allred** (Lavender) : data-backed cold email, built on 2B+ analyzed emails.
4. **Jed Mahrle** (Practical Prospecting) : lean outbound where human craft meets automation.
5. **Leslie Venetz** : omnichannel outbound; USA Today bestselling author; sharp BS detector.
6. **Nick Cegelski** (30MPC) : #1 sales podcast; *Cold Calling Sucks*, backed by 300M+ calls.
7. **Florin Tatulea** : GTM engineering; actually builds AI-agent outbound systems.
8. **Kyle Coleman** (ex-Copy.ai) : best on using AI to research and personalize at scale.
9. **Thibaut Souyris** : creative outreach (video, voice notes) that AI cannot fully copy.
10. **Becc Holland** (Flip the Script) : personalization (1:1) vs. relevance (1:many), the key idea.

### What I collected
- **25 LinkedIn posts across 9 authors**, organised one file per author.
- **6 video and talk transcripts** (Kyle Coleman, Jason Bay ~2,800 lines, Josh Braun x2, Becc Holland x2).
- **Newsletter and framework material**: the full 30MPC cold-calling framework plus Florin Tatulea's *Prospecting from the Trenches* summaries and a podcast.
- **10 fact-checked claims** in [`fact-check.md`](research/other/fact-check.md) and a synthesis in [`synthesis.md`](research/synthesis.md).

Every one of the 10 experts has at least one collected artifact, and most have two or more.

### How I collected it
- **`scripts/get_transcript.py`**, a small Python tool I wrote on top of `youtube-transcript-api`, pulls a video's transcript into clean Markdown organised by author.
- Public newsletters and frameworks were fetched directly. Paywalled Substacks were captured as public summaries and backed up with the author's LinkedIn.
- LinkedIn posts were collected from public post URLs (the login-walled feed cannot be scraped reliably or within their ToS).
- Claims in the fact-check were verified against independent primary sources (acquisition announcements, retailers, company sites).

### Issues I ran into and how I solved them
- **`youtube-transcript-api` changed its API in v1.x.** The old `.get_transcript()` static method was gone. I checked the installed version's methods, found it now uses an instance method (`YouTubeTranscriptApi().fetch()`), and updated the script.
- **Paywalled newsletters** (Jed Mahrle, Florin Tatulea). Only previews are public. Rather than fake completeness, I saved the public summaries, noted the paywall, and leaned on their LinkedIn for substance.
- **LinkedIn is login-walled.** Scraping the feed breaks against their ToS and is unreliable, so I collected from public post URLs and documented the choice.

### From research to a playbook
[`synthesis.md`](research/synthesis.md) turns all of this into a point of view: AI handles relevance at scale, humans win on true 1:1 personalization for high-value accounts. That tiered model, plus the call framework from 30MPC, is the skeleton of the cold-outreach playbook this research is meant to support.

---

## Step 1: AI Tooling Setup

### Tools installed
- **Cursor IDE**: AI-powered code editor (cursor.com).
- **Claude Code** (Cursor extension): AI coding assistant by Anthropic, authenticated via my Claude.ai account.
- **Codex** (Cursor extension): AI coding agent by OpenAI, installed manually after the extension panel install failed.

### Steps completed
1. Downloaded and installed Cursor IDE on macOS (Apple Silicon).
2. Installed the Claude Code extension and authenticated with my Claude.ai account.
3. Installed the Codex extension and authenticated with my ChatGPT account.
4. Created a public GitHub repository.
5. Opened the repository in Cursor.
6. Created this README documenting tools, steps, and issues.

### Issues encountered and how I solved them
**Codex extension.** Searching "Codex" in Cursor's Extensions panel found "Codex, OpenAI's coding agent," but installation failed with *"Error while installing 'Codex, OpenAI's coding agent' extension."* I resolved it by running the manual install from OpenAI's site via terminal, after which the extension worked.

**Claude Code sign-in.** The extension did not automatically open a browser for authentication. I resolved it by triggering sign-in manually via `Ctrl+Shift+P` then "Claude Code: Sign In".

### Notes
I approach problems the way I'd approach any growth challenge: figure out what's needed, try to solve it, document what happened, and flag blockers clearly rather than guessing blindly.
