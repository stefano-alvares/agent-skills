# Astro Premium Storefront Reference

Use this reference when the repo follows the same shape as The One Jewellery Store:

- Astro app lives in `web/`
- context files live at repo root: `PRODUCT.md`, `DESIGN.md`
- screenshot helper lives at `web/tools/shot.mjs`
- baseline proof commands are `npm test`, `npm run build`, `node tools/crawl.mjs`

## Intended stack order

1. `impeccable` for context, shaping, critique
2. implementation pass
3. `render-loop` for desktop and mobile screenshots
4. `make-interfaces-feel-better` for tactile corrections
5. `impeccable critique` or `impeccable polish`
6. repo proof commands

## Render commands

From `web/`:

```bash
npm run dev -- --host 127.0.0.1
```

Desktop screenshot example:

```bash
node tools/shot.mjs http://127.0.0.1:4321/ /tmp/render-home-desktop.png 1440 1080 full
```

Mobile screenshot example:

```bash
node tools/shot.mjs http://127.0.0.1:4321/ /tmp/render-home-mobile.png 390 844 full
```

Route example:

```bash
node tools/shot.mjs http://127.0.0.1:4321/pieces/example-handle /tmp/render-pdp-desktop.png 1440 1080 full
node tools/shot.mjs http://127.0.0.1:4321/pieces/example-handle /tmp/render-pdp-mobile.png 390 844 full
```

If `astro dev` cannot bind in the current sandbox, say so plainly. Do not fake the render step.

## Screenshot review checklist

For this storefront shape, always check:

- header at top and after scroll
- mobile navigation open state
- hero proportion and copy measure
- product card hover and acquired state
- cart drawer overlay and lock state
- PDP purchase rail and disclosure legibility
- footer density on mobile

## Repo proof commands

From `web/`:

```bash
npm test
npm run build
node tools/crawl.mjs
```

These do not replace screenshots. They prove regressions did not break the app while the screenshots prove the UI actually looks right.
