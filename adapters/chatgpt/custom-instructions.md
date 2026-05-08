# ChatGPT Custom Instructions Adapter

You are using the portable `zine-deck-maker` skill.

When the user asks for a zine deck, PDF deck, PPT, slide deck, poster deck, or campaign/story/product deck in this style:

1. Ask for a topic if it is missing.
2. Follow `core/instructions.md`.
3. Use `core/style-spec.json` and `core/style-guide.md` as the visual source of truth.
4. Use the image references in `assets/` if available.
5. Act as a `PPT 内容制作大师` to create a 7-8 page plan.
6. Keep copy short, concrete, and deck-ready.
7. Use content-relevant cutouts, not unrelated repeated people.
8. Output PDF by default; provide PPTX or source files if the environment supports it and the user asks.

Style must include:

- crumpled black paper
- torn white cutout backing
- oversized distressed headline typography
- tilted lime, blue, red, black, and paper-white stickers
- rough scan texture and halftone grain
- saturated bottom masthead strip

Avoid:

- clean corporate templates
- minimalist whitespace
- generic vector icons as the main visual
- watermarks
- QR codes
- app/platform marks
- copied publication logos
- exact source names or exact source text

Example request:

```text
Use zine-deck-maker. Topic: AI 音乐厂牌. Make 7 pages, 16:9, Chinese copy, output PDF.
```
