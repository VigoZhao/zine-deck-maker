# Image Generation Provider Slot

This skill is provider-agnostic. It does not require GPT-image, OpenAI, or any single image model.

The example outputs in this repository were created in an environment with GPT-image support. That is an implementation detail, not a dependency. Other users can plug in their own image generation or design workflow.

## Supported Routes

Use whichever route the host environment supports:

- GPT-image or another OpenAI image model
- Midjourney
- Flux
- Stable Diffusion / SDXL
- Ideogram
- Adobe Firefly
- Internal company image models
- Manual design in Photoshop, Figma, Canva, or another editor

## Provider Input Fields

When a user or platform supports configuration, accept these fields:

```yaml
image_generation_provider: "<provider name>"
image_generation_model: "<model name or version>"
image_generation_method: "<native tool | external prompt export | manual design>"
image_prompt_language: "<English recommended for many image models; Chinese is fine if supported>"
output_image_count: "one background plate per page"
```

## Fallback Behavior

If the current product cannot generate images:

1. Still create the 7-8 page content plan.
2. Produce one visual prompt per page.
3. Include the required aspect ratio.
4. Include the content-relevant cutout, props, style rules, and negative prompt.
5. Tell the user to paste those prompts into their chosen image model.
6. If deck/PDF generation is also unavailable, provide layout instructions instead of claiming completion.

## Prompt Adaptation Rules

Keep the core visual grammar stable across models:

- crumpled black paper
- torn white backing
- content-relevant cutout
- huge distressed headline area
- tilted lime/blue/red stickers
- rough photocopy grain
- saturated bottom masthead strip

Avoid provider-specific tokens unless the user names that provider. Do not mention a model name in the output unless the user requested it.

## Per-Page Prompt Contract

For each page, the agent should be able to export:

```text
Page:
Aspect ratio:
Main cutout:
Supporting props:
Headline area:
Sticker labels:
Bottom masthead:
Style:
Negative prompt:
Text handling:
```

Recommended text handling for image models: ask for blank or abstract label blocks, then add final readable text in the deck tool. This avoids hallucinated text, misspellings, watermarks, and fake logos.
