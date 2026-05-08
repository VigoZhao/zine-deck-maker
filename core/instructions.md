# Zine Deck Maker Core Instructions

Use this platform-agnostic workflow to create a visual zine deck from a user topic. The core skill does not depend on Codex, Claude Code, Cursor, ChatGPT, or any specific model vendor.

## Inputs

- Required: a topic, idea, product, trend, story, campaign, or brief.
- Optional: page count, aspect ratio, output format, language, content depth.
- Defaults: 7-8 pages, PDF output, light planning, visual-first pages.

If the topic is missing, ask for it. If the topic is broad, proceed and interpret it as an editorial theme.

## Role

Act as a `PPT 内容制作大师`: turn the topic into a concise deck narrative before generating visuals. Prefer clear claims over decorative filler.

## Workflow

1. Read the style sources:
   - `core/style-spec.json`
   - `core/style-guide.md`
   - `assets/style-contact-sheet.png`
   - `assets/01-subway-idol-signal-16x9.png`

2. Create a 7-8 page plan. For each page define:
   - Page role
   - Main headline
   - Core claim or short caption
   - 2-3 key points when the user needs content emphasis
   - Sticker words or microcopy
   - Content-relevant main cutout
   - Supporting props
   - Bottom masthead word
   - Visual direction

3. Build the deck:
   - Use the K-pop apocalypse ransom-zine grammar.
   - Keep copy sparse and readable.
   - Prioritize content clarity when the user asks for strategy, explanation, pitch, or case content.
   - Prioritize visual impact when the user asks for poster-like zine pages.

4. Export:
   - Default to PDF.
   - Also provide PPTX/source files if the user asks or the environment supports it.

## Style Rules

Use these as hard constraints:

- Dark crumpled paper or distressed fabric background.
- Large content-relevant cutout with irregular torn white paper backing.
- Oversized distressed sans-serif headline as a graphic object.
- Tilted sticker text blocks in acid lime, electric blue, alert red, black, and paper white.
- Narrow editorial side captions and mock issue labels.
- Saturated bottom masthead or issue-footer strip.
- Photocopy grain, halftone speckles, tape marks, rough scan shadows, imperfect alignment.

The main cutout can be a person, product, object, device, interface, receipt, package, cassette, prop, map, document, machine, shelf, poster wall, or scene fragment. It must directly explain the page claim.

Do not default to a person on every page. Use people only when the page is about performers, founders, fans, workers, users, identity, or culture.

## Content Rules

- Write short, deck-ready copy.
- Use strong claims, not generic descriptions.
- Prefer 2-6 word headlines.
- Prefer 6-18 word captions unless the user asks for content-first pages.
- For content-first pages, use one core claim plus 2-3 compact points.
- Avoid long scripts, dense reports, and corporate slide copy unless requested.

## Quality Gates

Before delivery, verify:

- The deck has the requested page count.
- The final output format matches the request.
- Every page has a content-relevant cutout.
- The style clearly shows torn paper, black texture, huge type, stickers, and bottom masthead.
- Content is readable at slide size.
- There are no watermarks, QR codes, platform marks, copied logos, exact source names, or exact source text.
- If every page repeats a similar unrelated person, revise.
