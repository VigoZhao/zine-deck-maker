---
name: zine-deck-maker
description: "Create visually driven 7-8 page PDF or PPT zine decks from a user topic using the portable K-pop apocalypse ransom-zine style. Use when Codex is asked to turn a topic, idea, product, trend, campaign, story, or brief into a PDF, deck, PPT, slide deck, poster deck, or zine in this style."
---

# Zine Deck Maker

This root `SKILL.md` exists for direct Codex installation compatibility.

The platform-neutral skill lives in:

- `core/instructions.md`
- `core/style-spec.json`
- `core/style-guide.md`
- `core/prompt-template.md`

The platform adapters live in:

- `adapters/codex/SKILL.md`
- `adapters/claude-code/agent.md`
- `adapters/claude-code/command.md`
- `adapters/cursor/rules.md`
- `adapters/chatgpt/custom-instructions.md`
- `adapters/generic/system-prompt.md`

## Workflow

1. If the user did not provide a topic, ask for one.
2. Read `core/instructions.md`.
3. Read `core/style-spec.json` and `core/style-guide.md` when designing or prompting visuals.
4. Inspect `assets/style-contact-sheet.png` and `assets/01-subway-idol-signal-16x9.png` when visual fidelity matters.
5. Plan 7-8 pages as a `PPT 内容制作大师`.
6. Generate a PDF-first zine deck; provide PPTX too if requested.
7. Run the quality gates from `core/instructions.md` before final delivery.

## Hard Rules

- Use content-relevant cutouts on every page.
- Do not default to a person on every page.
- Preserve the K-pop apocalypse ransom-zine grammar: crumpled black texture, torn white paper, huge distressed type, tilted stickers, scan grain, and a saturated bottom masthead.
- Keep copy short and deck-ready.
- Avoid watermarks, QR codes, platform marks, app logos, copied publication logos, exact source names, and exact source text.
