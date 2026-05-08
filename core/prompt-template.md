# Prompt Templates

## User Request Template

```text
Use zine-deck-maker.
Topic: <topic>
Pages: <7 or 8>
Aspect ratio: <9:16 or 16:9>
Language: <Chinese or English>
Output: <PDF, PPTX, or both>
Content depth: <visual-first or content-first>
```

## Content Planning Prompt

```text
You are a PPT 内容制作大师.

Turn the topic below into a 7-8 page zine deck plan.

Topic: <topic>
Audience: <audience if known>
Language: <language>
Content depth: <visual-first or content-first>

For each page, provide:
1. Page role
2. Headline
3. Core claim or caption
4. 2-3 key points if content-first
5. Sticker words
6. Main content-relevant cutout
7. Supporting props
8. Bottom masthead word
9. Visual direction

Keep copy short, specific, and deck-ready. Avoid generic business language.
```

## Visual Generation Prompt

```text
Create a <aspect ratio> K-pop apocalypse ransom-zine slide background for:

Topic: <topic>
Page: <page number and role>
Main content-relevant cutout: <cutout>
Supporting props: <props>

Use dark crumpled black paper, torn white paper backing, distressed photocopy grain, halftone speckles, tilted sticker blocks in acid lime, electric blue, alert red, paper white, and ink black. Add a saturated bottom masthead band and rough scan shadows.

Leave clear areas for editable text overlay. Do not include readable text unless explicitly provided. Do not include watermarks, QR codes, platform marks, app logos, copied publication logos, exact source names, or exact source text.
```

## QA Prompt

```text
Review the deck against zine-deck-maker quality gates:
- requested page count
- requested output format
- readable content hierarchy
- content-relevant cutout on every page
- black crumpled texture, torn paper, distressed headline, stickers, bottom masthead
- no unrelated repeated person
- no forbidden watermarks, QR codes, platform marks, copied logos, exact source names, or exact source text

List pass/fail and revise failed pages before delivery.
```
