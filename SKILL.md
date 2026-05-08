---
name: zine-deck-maker
description: "Create visually driven 7-8 page PDF zine decks from a user topic using the bundled K-pop apocalypse ransom-zine style, including photo/AI-image cutouts, oversized distressed typography, torn paper collage, stickers, and bottom masthead bands. Use when Codex is asked to turn a topic, idea, product, trend, campaign, story, or brief into a PDF, deck, PPT, slide deck, poster deck, or zine in this style."
---

# Zine Deck Maker

## Overview

Turn a user-provided topic into a 7-8 page PDF deck with light content planning and a maximalist K-pop apocalypse ransom-zine visual system. Use `references/style-spec.json` and `references/style-guide.md` as the source of truth. Use the image assets as visual references:

- `assets/01-subway-idol-signal-16x9.png`: strongest single-slide 16:9 reference.
- `assets/style-contact-sheet.png`: multi-case reference across 9:16 and 16:9.
- Other PNG files in `assets/`: individual 9:16 and 16:9 sample renders for the four documented style cases.

Default to PDF output only. Use an editable deck or intermediate source file only as a working artifact unless the user explicitly asks for PPTX or source files too.

## Workflow

1. Confirm the topic.
   - If the user did not provide a topic, ask for one concise topic or brief.
   - If the topic is broad, proceed without asking; interpret it as a visual editorial theme.

2. Load the style references.
   - Read `references/style-spec.json`.
   - Read `references/style-guide.md` when tuning prompts or composition.
   - Inspect the asset images when visual fidelity matters, especially for public examples or user-facing final decks.

3. Create a light 7-8 page content plan as a PPT content master.
   - Adopt the role: `PPT 内容制作大师`.
   - Generate 7 or 8 page concepts with short, deck-ready copy.
   - For each page, define: page role, main headline, short caption, sticker/microcopy words, visual direction, subject/cutout, prop, and bottom masthead word.
   - Keep copy punchy and sparse. Do not write a long article, speaker script, or dense business report unless the user asks.
   - Prefer a narrative arc: cover, tension/context, key idea, 3-4 themed spreads, closing punchline or manifesto.
   - For abstract topics, personify the idea as a performer, clerk, stylist, courier, idol, dancer, or youth-culture character so the page still has a strong photo cutout.

4. Produce the PDF deck.
   - Use the bundled style spec to drive every page.
   - Prefer a 9:16 poster-zine deck unless the user requests widescreen.
   - Build visually first: large photo/AI-image portrait cutout or product cutout, oversized distressed headline, sticker labels, side captions, bottom masthead strip, tactile paper texture.
   - Use generated raster imagery when needed. Do not substitute simple geometric icons for the main subject.
   - Use the Presentations workflow/tools when available for reliable deck creation, rendering, visual QA, and PDF export.
   - Deliver the final PDF path. Mention any working PPTX/source only if it is useful or requested.

## Style Rules

Load `references/style-spec.json` before designing pages. Treat these constraints as mandatory:

- Use crumpled black or distressed fabric backgrounds.
- Use a large central or center-right photo-real portrait/character/product cutout with thick irregular torn white paper backing.
- Use huge distressed sans-serif headline typography as a graphic object. It should occupy major canvas area and overlap the cutout/backing.
- Use tilted sticker text blocks in acid lime, electric blue, alert red, black, and paper white.
- Use narrow editorial side captions, small mock issue labels, barcode stripes, and a thumbnail/inset when useful.
- Use acid lime, electric blue, alert red, paper white, charcoal, and ink black as the dominant palette.
- Add photocopy grain, halftone speckles, rough scan shadows, tape marks, and imperfect alignment.
- Anchor pages with a bold bottom masthead or issue-footer strip.
- Keep subject/idea, headline, sticker words, and footer as the main hierarchy.
- Avoid clean corporate layouts, minimalist whitespace, soft pastel lifestyle palettes, elegant serif mastheads, glossy 3D type, watermarks, usernames, creator IDs, QR codes, app marks, copied publication logos, exact source names, or exact source text.

## Visual Fidelity Guardrails

Do not accept an output as style-faithful unless it clearly has all of these:

- A photo-real or AI-image cutout subject with torn white paper border.
- A huge distressed headline comparable to `STATIC POP`, `BUNKER FIT`, `RIPPED SIGNAL`, or `LAST LOOK`.
- At least three tilted sticker labels.
- Dense scanned paper texture, wrinkles, halftone, and rough edges.
- A saturated bottom masthead band, usually electric blue, lime, or red.

If a page only has black background, neon colors, vector shapes, and footer strips, it has not preserved this style. Revise before delivery.

## Content Plan Format

Use this compact structure internally before building:

```markdown
1. Page role:
   Headline:
   Caption:
   Sticker words:
   Subject/cutout:
   Prop:
   Bottom masthead:
   Visual direction:
```

Headlines should usually be 2-6 words. Captions should usually be 6-18 words. Sticker words should be fragments, labels, mock issue lines, lyric-like shards, or styling notes.

## Output Checks

Before final delivery, verify:

- The deck has 7 or 8 pages.
- The final artifact is a PDF unless the user asked for another format.
- Text is short enough to read as poster/deck copy.
- Every page visibly follows the zine style rather than a corporate or minimalist slide template.
- Every page has a strong cutout subject or product image, not just geometric symbols.
- No forbidden watermarks, QR codes, platform marks, copied logos, exact source names, or exact source text appear.
