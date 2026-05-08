---
name: zine-deck-maker
description: "Create visually driven 7-8 page PDF zine decks from a user topic using the bundled K-pop apocalypse ransom-zine style. Use when Codex is asked to turn a topic, idea, product, trend, campaign, story, or brief into a PDF, deck, PPT, slide deck, or zine in this style, including requests like '用这个风格做一组 PDF', '生成 zine 风格 PPT', '基于主题做 7-8 页视觉 deck', or '做成 ransom zine 海报感的演示文稿'."
---

# Zine Deck Maker

## Overview

Turn a user-provided topic into a 7-8 page PDF deck with light content planning and a maximalist ransom-zine visual system. Use `references/style-spec.json` as the source of truth for palette, layout, typography, texture, negative prompt, and avoid-list.

Default to PDF output only. Use an editable deck or intermediate source file only as a working artifact unless the user explicitly asks for PPTX or source files too.

## Workflow

1. Confirm the topic.
   - If the user did not provide a topic, ask for one concise topic or brief.
   - If the topic is broad, proceed without asking; interpret it as a visual editorial theme.

2. Create a light 7-8 page content plan as a PPT content master.
   - Adopt the role: `PPT 内容制作大师`.
   - Generate 7 or 8 page concepts with short, deck-ready copy.
   - For each page, define: page role, main headline, short caption, sticker/microcopy words, and visual direction.
   - Keep copy punchy and sparse. Do not write a long article, speaker script, or dense business report unless the user asks.
   - Prefer a narrative arc: cover, tension/context, key idea, 3-4 themed spreads, closing punchline or manifesto.

3. Produce the PDF deck.
   - Use the bundled style spec to drive every page.
   - Prefer a 9:16 poster-zine deck unless the user requests widescreen.
   - Build visually first: large portrait or symbolic cutout, oversized headline, sticker labels, side captions, bottom masthead strip, tactile paper texture.
   - Use the Presentations workflow/tools when available for reliable deck creation, rendering, visual QA, and PDF export.
   - Deliver the final PDF path. Mention any working PPTX/source only if it is useful or requested.

## Style Rules

Load `references/style-spec.json` before designing pages. Treat these constraints as mandatory:

- Use crumpled black or distressed fabric backgrounds.
- Use torn white portrait backing or object cutouts with rough paper edges.
- Use heavy warped sans-serif, tilted labels, sticker text, ransom-note layering, and narrow editorial side captions.
- Use acid lime, electric blue, alert red, paper white, charcoal, and ink black as the dominant palette.
- Add photocopy grain, halftone speckles, rough scan shadows, tape marks, and imperfect alignment.
- Anchor pages with a bold bottom masthead or issue-footer strip.
- Keep subject/idea, headline, sticker words, and footer as the main hierarchy.
- Avoid clean corporate layouts, minimalist whitespace, soft pastel lifestyle palettes, elegant serif mastheads, glossy 3D type, watermarks, usernames, creator IDs, QR codes, app marks, copied publication logos, exact source names, or exact source text.

## Content Plan Format

Use this compact structure internally before building:

```markdown
1. Page role:
   Headline:
   Caption:
   Sticker words:
   Visual direction:
```

Headlines should usually be 2-6 words. Captions should usually be 6-18 words. Sticker words should be fragments, labels, mock issue lines, lyric-like shards, or styling notes.

## Output Checks

Before final delivery, verify:

- The deck has 7 or 8 pages.
- The final artifact is a PDF unless the user asked for another format.
- Text is short enough to read as poster/deck copy.
- Every page visibly follows the zine style rather than a corporate or minimalist slide template.
- No forbidden watermarks, QR codes, platform marks, copied logos, exact source names, or exact source text appear.
