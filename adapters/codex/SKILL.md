---
name: zine-deck-maker
description: "Create visually driven 7-8 page PDF or PPT zine decks from a user topic using the portable K-pop apocalypse ransom-zine style. Use when Codex is asked to turn a topic, idea, product, trend, campaign, story, or brief into a PDF, deck, PPT, slide deck, poster deck, or zine in this style."
---

# Zine Deck Maker For Codex

Use the platform-neutral core files:

- `core/instructions.md`
- `core/style-spec.json`
- `core/style-guide.md`
- `core/prompt-template.md`

Use visual references:

- `assets/01-subway-idol-signal-16x9.png`
- `assets/style-contact-sheet.png`

## Workflow

1. If the user did not provide a topic, ask for one.
2. Read `core/instructions.md` and the style references when visual fidelity matters.
3. Plan 7-8 pages as a `PPT 内容制作大师`.
4. Generate a PDF-first zine deck. If the user asks for PPTX too, provide both.
5. Verify all quality gates in `core/instructions.md`.

## Codex Notes

- Use image generation for raster plates when needed.
- Use presentation/PDF tooling when available for deck rendering and QA.
- Keep generated project assets inside the current workspace.
- Root `SKILL.md` is kept for direct Codex installation compatibility.
