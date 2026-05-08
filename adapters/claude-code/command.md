# /zine-deck-maker

Create a 7-8 page zine deck from the user's topic using this repository's portable zine-deck-maker core.

Read:

- `core/instructions.md`
- `core/style-spec.json`
- `core/style-guide.md`
- `core/image-generation.md`

Use visual references in `assets/`.

Expected user arguments:

```text
主题：<topic>，做 <7 or 8> 页，<9:16 or 16:9>，<中文 or English>，输出 <PDF/PPTX/both>
```

Process:

1. Parse topic, page count, aspect ratio, language, and output format.
2. If topic is missing, ask for it.
3. Plan the deck as a `PPT 内容制作大师`.
4. Generate pages with content-relevant cutouts, huge distressed titles, torn paper, stickers, crumpled black texture, and bottom masthead bands.
5. Use the available image provider, or export image prompts for the user's own model if image generation is unavailable.
6. Export PDF by default.
7. Check quality gates before final response.

Example:

```text
/zine-deck-maker 主题：AI 音乐厂牌，做 7 页，16:9，中文，输出 PDF
```
