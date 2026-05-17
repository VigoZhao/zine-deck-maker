---
name: zine-deck-maker
description: "Create visually driven 7-8 page PDF zine decks from a topic, idea, product, trend, campaign, story, or brief using the bundled K-pop apocalypse ransom-zine style. Use for PDF/deck/PPT/slide/poster-zine requests that need content-relevant cutouts, distressed typography, torn paper, stickers, scan texture, and bottom masthead bands. Not for ordinary business decks, generic image prompts, single images, or unrelated visual styles."
---

# Zine Deck Maker

## Default Goal

Turn a user-provided topic into a 7-8 page PDF deck with light content planning and the bundled maximalist K-pop apocalypse ransom-zine visual system. Default to a 7-page 9:16 poster-zine PDF unless the user's brief needs 8 pages or explicitly asks for widescreen, PPTX, or source files.

## Trigger Boundary

Use when:

- The user asks to turn a topic, idea, product, trend, campaign, story, brief, or research angle into a PDF, deck, PPT, slide deck, poster deck, or zine.
- The desired output is this bundled K-pop apocalypse ransom-zine style or the user explicitly invokes `$zine-deck-maker`.
- The task needs both short content planning and a visually driven final artifact.

Not for:

- Ordinary business decks, consulting slides, pitch decks, minimalist presentations, or long-form reports.
- Generic image prompt writing, style extraction, single poster/image generation, or reusable style-package creation.
- Decks in unrelated visual systems unless the user asks to adapt this exact zine method.

Do not silently chain to other skills. If the user wants style extraction, source research, article writing, X posts, or a separate image-generation pack, finish this deck task first or ask before changing workflow.

## Reference Routing

- Always read `references/style-spec.json` before designing pages.
- Read `references/style-guide.md` when tuning prompts, composition, copy tone, or acceptance criteria.
- Inspect `assets/style-contact-sheet.png` for multi-case style calibration.
- Inspect `assets/01-subway-idol-signal-16x9.png` when the user requests widescreen output.
- Use the other PNG files in `assets/` as visual examples only; do not copy exact text, names, or marks from them.

The variable style layer belongs in `references/` and `assets/`. If the visual system changes, update those files rather than hardcoding a new style interpretation in this file.

## Default Behavior

- Proceed with the provided topic; ask one concise question only if no topic or brief is present.
- Interpret broad topics as editorial themes instead of blocking for clarification.
- Generate sparse deck copy, not a full article or speaker script.
- Prefer 9:16 PDF output.
- Treat PPTX, editable source, and intermediate files as working artifacts unless explicitly requested.

## Manual Modes

Only switch modes when the user asks:

- Widescreen mode: create a 16:9 deck and use the 16:9 reference assets.
- Editable mode: deliver PPTX/source alongside the PDF.
- Expanded mode: use 8 pages when the story needs the extra spread.
- Style-maintenance mode: update `references/` or `assets/` if the bundled style system itself is being revised.

## Core Workflow

1. Confirm the topic only when missing.

2. Load the style references.
   - Read `references/style-spec.json`.
   - Read `references/style-guide.md` when tuning prompts or composition.
   - Inspect the asset images when visual fidelity matters, especially for public examples or user-facing final decks.

3. Create a light 7-8 page content plan as a PPT content master.
   - Adopt the role: `PPT 内容制作大师`.
   - Generate 7 or 8 page concepts with short, deck-ready copy.
   - For each page, define: page role, main headline, short caption, sticker/microcopy words, content-relevant main cutout, supporting props, and bottom masthead word.
   - Keep copy punchy and sparse. Do not write a long article, speaker script, or dense business report unless the user asks.
   - Prefer a narrative arc: cover, tension/context, key idea, 3-4 themed spreads, closing punchline or manifesto.
   - For abstract topics, choose a concrete visual noun that explains the page: object, place, machine, interface, product, receipt, cassette, device, costume, shelf, poster wall, performer, fan, founder, clerk, or other relevant cutout.
   - Do not default to a person on every page. Use people only when the page is about performers, users, founders, fans, workers, identity, or culture.

4. Produce the PDF deck.
   - Use the bundled style spec to drive every page.
   - Build visually first: large content-relevant cutout, oversized distressed headline, sticker labels, side captions, bottom masthead strip, tactile paper texture.
   - Use generated raster imagery when needed. Do not substitute simple geometric icons for the main visual.
   - Use the Presentations workflow/tools when available for reliable deck creation, rendering, visual QA, and PDF export.
   - Deliver the final PDF path. Mention any working PPTX/source only if it is useful or requested.

## Visual Acceptance Gates

Do not accept an output as style-faithful unless each page clearly has:

- A content-relevant person, object, product, device, place, interface, receipt, package, prop, or scene cutout with torn white paper backing.
- A huge distressed headline comparable to `STATIC POP`, `BUNKER FIT`, `RIPPED SIGNAL`, or `LAST LOOK`.
- At least three tilted sticker labels.
- Dense scanned paper texture, wrinkles, halftone, and rough edges.
- A saturated bottom masthead band, usually electric blue, lime, or red.

Avoid clean corporate layouts, minimalist whitespace, soft pastel lifestyle palettes, elegant serif mastheads, glossy 3D type, watermarks, usernames, creator IDs, QR codes, app marks, copied publication logos, exact source names, or exact source text.

If a page only has black background, neon colors, vector shapes, and footer strips, it has not preserved this style. If every page repeats a similar person who does not explain the slide claim, the deck has not preserved the content logic. Revise before delivery.

## Content Plan Format

Use this compact structure internally before building:

```markdown
1. Page role:
   Headline:
   Caption:
   Sticker words:
   Main cutout:
   Supporting props:
   Bottom masthead:
   Visual direction:
```

Headlines should usually be 2-6 words. Captions should usually be 6-18 words. Sticker words should be fragments, labels, mock issue lines, lyric-like shards, or styling notes.

## Validation

Before final delivery, verify:

- The deck has 7 or 8 pages.
- The final artifact is a PDF unless the user asked for another format.
- Text is short enough to read as poster/deck copy.
- Every page visibly follows the zine style rather than a corporate or minimalist slide template.
- Every page has a strong content-relevant cutout, not just geometric symbols and not an unrelated repeated person.
- No forbidden watermarks, QR codes, platform marks, copied logos, exact source names, or exact source text appear.

When a PDF exists locally, run the deterministic page-count check:

```shell
python3 /Users/zhaoweigang/.codex/skills/zine-deck-maker/scripts/validate_zine_pdf.py /path/to/deck.pdf
```

This script only verifies file shape and 7-8 PDF pages. Visual fidelity still requires rendered-page inspection.
