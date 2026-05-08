# Cursor Rules For Zine Deck Maker

When the user asks to create a zine deck, poster deck, PDF deck, PPT deck, or slide deck in this style, use the portable skill files:

- `core/instructions.md`
- `core/style-spec.json`
- `core/style-guide.md`
- `core/prompt-template.md`
- `core/image-generation.md`

Rules:

- Ask for a topic if missing.
- Default to 7-8 pages and PDF output.
- Use Chinese or English based on the user request.
- Create a concise content plan before visuals.
- Every page must have a content-relevant cutout.
- Use the available image provider or export page-by-page prompts for the user's chosen image model.
- Preserve the K-pop apocalypse ransom-zine grammar: crumpled black texture, torn white paper, huge distressed type, stickers, red/lime/blue accents, bottom masthead.
- Do not use unrelated repeated people.
- Do not include watermarks, QR codes, platform marks, app logos, copied publication logos, exact source names, or exact source text.

Suggested invocation:

```text
Use zine-deck-maker. Topic: AI 音乐厂牌. Make 7 pages, 16:9, Chinese, output PDF.
```
