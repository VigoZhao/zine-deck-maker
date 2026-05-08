# K-Pop Apocalypse Ransom Zine Style

## Style Summary

This style is a maximalist K-pop fashion zine collage system. It combines a close portrait cutout, torn white paper backing, crumpled black texture, skewed ransom-note typography, electric sticker blocks, a red graphic symbol near the face, and a loud bottom masthead strip.

The reference reads like a DIY pop-punk fashion magazine cover made after the end of the world: chaotic, playful, sarcastic, tactile, and still obsessed with styling. The reusable system should keep the collage energy while avoiding copied names, platform marks, watermarks, QR codes, creator IDs, or exact source text.

## Core Visual Identity

- Central portrait cutout with an uneven torn-paper white border.
- Dark crumpled-paper or distressed fabric background.
- Oversized warped headline text used as a graphic object.
- Tilted sticker blocks in acid lime, electric blue, red, black, and white.
- Small editorial side captions in narrow white text.
- Bold bottom masthead strip with a thumbnail inset and giant display word.
- Photocopy grain, halftone speckles, paper wrinkles, rough shadows, and print misregistration.

## Visual Deconstruction

### Overall Style Category

K-pop fashion zine poster, Y2K pop-punk collage, apocalypse editorial cover, ransom-note magazine layout, DIY street fashion flyer.

### Composition And Layout

The subject dominates the lower center of the frame. The top and side areas are packed with loud sticker-like words, diagonal banners, and small caption columns. A saturated footer strip acts like a magazine masthead and gives the poster a strong base. Layer order should feel physical: dark paper, torn backing, portrait, stickers, star or symbol, captions, footer.

### Subject Placement

Use a tight portrait or upper-body crop. The cutout should sit in front of a white torn-paper shape and overlap nearby text. Hair strands, shoulders, and paper edges can break into the surrounding layout, but the face should remain the visual anchor.

### Camera Angle Or Perspective

Straight-on or slightly low flash portrait. The subject can look off-frame, upward, or sideways. The pose should feel candid and stylized rather than polished.

### Typography Style

Typography is intentionally unstable. Use warped heavy sans-serif headlines, condensed sticker words, italicized tilted labels, and mixed scale type. Main text should feel pasted into place by hand. Small copy should be narrow, dense, and editorial.

### Color Palette

| Role | Hex |
|---|---|
| Crumpled black | `#171717` |
| Charcoal gray | `#3A3A3A` |
| Paper white | `#F5F3EE` |
| Acid lime | `#A8F04A` |
| Electric blue | `#1713F2` |
| Alert red | `#F2053A` |
| Ink black | `#050505` |
| Warm skin highlight | `#F2B69B` |

### Graphic Elements

- Torn white portrait backing.
- Diagonal lime banner.
- Blue sticker tabs.
- Red star or warning symbol near the face.
- Black-and-white Pop-style word blocks.
- Side editorial captions.
- Bottom masthead strip with a small inset portrait or thumbnail.
- Barcode stripes, arrows, paper shards, and rough sticker labels.

### Texture And Finish

The finish should look scanned and physical. Use crumpled paper, Xerox noise, halftone speckles, rough shadows, uneven cutout edges, and slight print offset. Avoid clean vector polish.

### Lighting

The subject should feel flash-lit with glossy face highlights, bright accessories, and crisp edges. The background should stay flat, dark, wrinkled, and gritty.

### Mood And Cultural Reference

Rebellious K-pop styling, post-apocalyptic fashion play, Y2K pop-punk graphics, cut-and-paste zine culture, underground magazine covers, and sarcastic youth editorial design.

## Reusable Design Rules

1. Begin with a dark crumpled texture.
2. Add a large central portrait with a torn white sticker outline.
3. Use one oversized headline as a graphic layer, not a clean title.
4. Add multiple tilted sticker labels in lime, blue, red, black, and white.
5. Keep side captions short and dense.
6. Use a saturated footer strip as a masthead or issue band.
7. Add one bold symbol near the face, such as a red star or warning mark.
8. Preserve a rough scanned-paper finish.

## Things To Avoid

- Minimalist poster design.
- Luxury fashion cleanliness.
- Soft pastel lifestyle palettes.
- Smooth vector-only graphics.
- Glossy 3D typography.
- Elegant serif mastheads.
- Empty whitespace-heavy composition.
- Platform watermarks, usernames, creator IDs, QR codes, app marks, or copied publication logos.
- Exact source names, dates, and text.

## Environment Variables

```json
{
  "SUBJECT": "main subject, performer, model, musician, dancer, stylist, or youth-culture character",
  "SUBJECT_ACTION": "looking off-frame, posing with attitude, holding a prop, leaning into the camera, or standing in a cutout portrait pose",
  "PRODUCT_OR_PROP": "compact camera, wired earbuds, lip gloss, denim jacket, cassette, charm bag, safety pin accessory, or styling prop",
  "LOCATION": "studio wall, backstage corner, bedroom mirror, subway entrance, alley poster wall, roof landing, or DIY magazine set",
  "BACKGROUND_ELEMENTS": "crumpled black paper, distressed denim texture, torn white paper edges, photocopy grain, halftone noise, tape marks, and rough scanned shadows",
  "MAIN_TEXT": "oversized warped headline or sticker headline",
  "SECONDARY_TEXT": "short editorial caption, mock issue line, styling note, lyric-like fragment, or repeated microcopy",
  "ACCENT_SYMBOL": "red star, diagonal sticker block, torn label, arrow tab, barcode stripe, or paper shard",
  "WARDROBE_STYLE": "post-apocalyptic K-pop styling, distressed denim, glossy makeup, messy hair, bright accessory accents, layered streetwear",
  "ASPECT_RATIO": "9:16 or 16:9"
}
```

## Prompt Template

```text
Create a {ASPECT_RATIO} K-pop apocalypse ransom zine poster featuring {SUBJECT} {SUBJECT_ACTION}, styled in {WARDROBE_STYLE}, with {PRODUCT_OR_PROP}. Use a dark crumpled black paper background with {BACKGROUND_ELEMENTS}. Place the subject as a large central portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "{MAIN_TEXT}" as a tilted collage layer, plus smaller sticker blocks and side editorial captions reading "{SECONDARY_TEXT}". Use acid lime, electric blue, alert red, paper white, and ink black. Add {ACCENT_SYMBOL} near the portrait. Finish with a saturated bottom masthead strip, rough photocopy grain, halftone speckles, scan noise, uneven paper shadows, and DIY magazine collage energy. Do not include watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

## Negative Prompt

```text
minimalist design, clean corporate layout, smooth gradients, luxury editorial polish, pastel lifestyle palette, glossy 3D typography, elegant serif masthead, empty whitespace, platform watermark, username, QR code, creator ID, app logo, copied publication logo, exact source text, exact source name
```

## Example Cases

### Case 01: Subway Idol Signal

- Subject: underground pop performer
- Action: looking up and sideways with messy windblown hair
- Prop: wired earbuds and compact camera
- Location: subway entrance poster wall
- Background elements: crumpled black paper, torn labels, photocopy grain, tape shadows
- Main text: `STATIC POP`
- Secondary text: `late train beauty / no soft landing / signal still loud`
- Accent symbol: red star and blue sticker tab
- Wardrobe: distressed denim halter, silver clips, glossy makeup

9:16 prompt:

```text
Create a vertical 9:16 K-pop apocalypse ransom zine poster featuring an underground pop performer looking up and sideways with messy windblown hair, styled in a distressed denim halter, silver clips, glossy makeup, and wired earbuds, holding a compact camera. Use a dark crumpled black paper background with torn labels, photocopy grain, tape shadows, and rough scanned texture. Place the subject as a large central portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "STATIC POP" as a tilted collage layer, plus smaller sticker blocks and side editorial captions reading "late train beauty / no soft landing / signal still loud". Use acid lime, electric blue, alert red, paper white, and ink black. Add a red star and blue sticker tab near the portrait. Finish with a saturated bottom masthead strip, rough photocopy grain, halftone speckles, scan noise, uneven paper shadows, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

16:9 prompt:

```text
Create a horizontal 16:9 K-pop apocalypse ransom zine poster featuring an underground pop performer looking up and sideways with messy windblown hair, styled in a distressed denim halter, silver clips, glossy makeup, and wired earbuds, holding a compact camera. Use a dark crumpled black paper background with torn labels, photocopy grain, tape shadows, and rough scanned texture. Place the subject as a large center-right portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "STATIC POP" as a tilted collage layer across the left and top, plus smaller sticker blocks and side editorial captions reading "late train beauty / no soft landing / signal still loud". Use acid lime, electric blue, alert red, paper white, and ink black. Add a red star and blue sticker tab near the portrait. Finish with a saturated bottom masthead strip, rough photocopy grain, halftone speckles, scan noise, uneven paper shadows, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

### Case 02: Rooftop Bunker Stylist

- Subject: fashion stylist
- Action: leaning forward with a survival-pop pose
- Prop: charm bag and safety pin accessory
- Location: roof landing
- Background elements: charcoal paper folds, torn white scraps, distressed fabric texture
- Main text: `BUNKER FIT`
- Secondary text: `utility glamour / storm proof gloss / still on point`
- Accent symbol: diagonal lime banner and barcode stripe
- Wardrobe: ripped black jacket, neon scarf, patched skirt, glossy red lip

9:16 prompt:

```text
Create a vertical 9:16 K-pop apocalypse ransom zine poster featuring a fashion stylist leaning forward with a survival-pop pose, styled in a ripped black jacket, neon scarf, patched skirt, and glossy red lip, holding a charm bag with safety pin accessories. Use a dark crumpled black paper background with charcoal paper folds, torn white scraps, distressed fabric texture, photocopy grain, and rough scanned shadows. Place the subject as a large central portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "BUNKER FIT" as a tilted collage layer, plus smaller sticker blocks and side editorial captions reading "utility glamour / storm proof gloss / still on point". Use acid lime, electric blue, alert red, paper white, and ink black. Add a diagonal lime banner and barcode stripe near the portrait. Finish with a saturated bottom masthead strip, halftone speckles, scan noise, uneven paper shadows, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

16:9 prompt:

```text
Create a horizontal 16:9 K-pop apocalypse ransom zine poster featuring a fashion stylist leaning forward with a survival-pop pose, styled in a ripped black jacket, neon scarf, patched skirt, and glossy red lip, holding a charm bag with safety pin accessories. Use a dark crumpled black paper background with charcoal paper folds, torn white scraps, distressed fabric texture, photocopy grain, and rough scanned shadows. Place the subject as a large center-right portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "BUNKER FIT" as a tilted collage layer across the left and top, plus smaller sticker blocks and side editorial captions reading "utility glamour / storm proof gloss / still on point". Use acid lime, electric blue, alert red, paper white, and ink black. Add a diagonal lime banner and barcode stripe near the portrait. Finish with a saturated bottom masthead strip, halftone speckles, scan noise, uneven paper shadows, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

### Case 03: Mirror Room Vocalist

- Subject: bedroom vocalist
- Action: staring off-frame while fixing a hair clip
- Prop: lip gloss and cracked hand mirror
- Location: bedroom mirror set
- Background elements: black wrinkled backdrop, tape marks, paper scraps, scan grain
- Main text: `RIPPED SIGNAL`
- Secondary text: `gloss in the blackout / voice note / tomorrow cancelled`
- Accent symbol: alert red slash label and paper shards
- Wardrobe: yellow ribbon top, denim arm warmers, chrome earrings

9:16 prompt:

```text
Create a vertical 9:16 K-pop apocalypse ransom zine poster featuring a bedroom vocalist staring off-frame while fixing a hair clip, styled in a yellow ribbon top, denim arm warmers, chrome earrings, and glossy makeup, holding lip gloss and a cracked hand mirror. Use a dark crumpled black paper background with black wrinkled backdrop texture, tape marks, paper scraps, scan grain, and rough shadows. Place the subject as a large central portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "RIPPED SIGNAL" as a tilted collage layer, plus smaller sticker blocks and side editorial captions reading "gloss in the blackout / voice note / tomorrow cancelled". Use acid lime, electric blue, alert red, paper white, and ink black. Add an alert red slash label and paper shards near the portrait. Finish with a saturated bottom masthead strip, photocopy grain, halftone speckles, scan noise, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

16:9 prompt:

```text
Create a horizontal 16:9 K-pop apocalypse ransom zine poster featuring a bedroom vocalist staring off-frame while fixing a hair clip, styled in a yellow ribbon top, denim arm warmers, chrome earrings, and glossy makeup, holding lip gloss and a cracked hand mirror. Use a dark crumpled black paper background with black wrinkled backdrop texture, tape marks, paper scraps, scan grain, and rough shadows. Place the subject as a large center-right portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "RIPPED SIGNAL" as a tilted collage layer across the left and top, plus smaller sticker blocks and side editorial captions reading "gloss in the blackout / voice note / tomorrow cancelled". Use acid lime, electric blue, alert red, paper white, and ink black. Add an alert red slash label and paper shards near the portrait. Finish with a saturated bottom masthead strip, photocopy grain, halftone speckles, scan noise, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

### Case 04: Alley Choreography Note

- Subject: dance captain
- Action: pausing mid-rehearsal and looking past camera
- Prop: mini cassette recorder and fingerless gloves
- Location: alley poster wall
- Background elements: distressed black paper, torn stickers, photocopied fabric grain
- Main text: `LAST LOOK`
- Secondary text: `final take / ripped hem / radio weather warning`
- Accent symbol: blue out-tab and red star stamp
- Wardrobe: cropped denim vest, orange scarf, black ribbon ties, smudged eye makeup

9:16 prompt:

```text
Create a vertical 9:16 K-pop apocalypse ransom zine poster featuring a dance captain pausing mid-rehearsal and looking past camera, styled in a cropped denim vest, orange scarf, black ribbon ties, smudged eye makeup, and fingerless gloves, holding a mini cassette recorder. Use a dark crumpled black paper background with distressed black paper, torn stickers, photocopied fabric grain, rough halftone noise, and scanned shadows. Place the subject as a large central portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "LAST LOOK" as a tilted collage layer, plus smaller sticker blocks and side editorial captions reading "final take / ripped hem / radio weather warning". Use acid lime, electric blue, alert red, paper white, and ink black. Add a blue out-tab and red star stamp near the portrait. Finish with a saturated bottom masthead strip, photocopy grain, halftone speckles, scan noise, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

16:9 prompt:

```text
Create a horizontal 16:9 K-pop apocalypse ransom zine poster featuring a dance captain pausing mid-rehearsal and looking past camera, styled in a cropped denim vest, orange scarf, black ribbon ties, smudged eye makeup, and fingerless gloves, holding a mini cassette recorder. Use a dark crumpled black paper background with distressed black paper, torn stickers, photocopied fabric grain, rough halftone noise, and scanned shadows. Place the subject as a large center-right portrait cutout with a thick irregular torn white paper border. Add oversized warped display typography reading "LAST LOOK" as a tilted collage layer across the left and top, plus smaller sticker blocks and side editorial captions reading "final take / ripped hem / radio weather warning". Use acid lime, electric blue, alert red, paper white, and ink black. Add a blue out-tab and red star stamp near the portrait. Finish with a saturated bottom masthead strip, photocopy grain, halftone speckles, scan noise, and DIY magazine collage energy. No watermarks, usernames, creator IDs, QR codes, platform logos, app marks, copied publication logos, or exact source text.
```

## Generated Image Set

| Case | 9:16 | 16:9 |
|---|---|---|
| Subway Idol Signal | `01-subway-idol-signal-9x16.png` | `01-subway-idol-signal-16x9.png` |
| Rooftop Bunker Stylist | `02-rooftop-bunker-stylist-9x16.png` | `02-rooftop-bunker-stylist-16x9.png` |
| Mirror Room Vocalist | `03-mirror-room-vocalist-9x16.png` | `03-mirror-room-vocalist-16x9.png` |
| Alley Choreography Note | `04-alley-choreography-note-9x16.png` | `04-alley-choreography-note-16x9.png` |

Overview: `style-contact-sheet.png`

## Files

- `README.md`: style document, reusable prompt template, example cases, and image index.
- `style-spec.json`: structured machine-readable style system.
- Generated PNG samples: created directly with GPT-image and copied into this folder.
