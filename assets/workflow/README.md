# Homepage workflow animation

The animation follows one original paragraph through five editing moves. The same page stays in view as related facts join into complete sentences and the paragraph develops from method to protocol to result. The complete [input, revision, and reasons](../../examples/workflow.md) are also available as text.

Editing frames keep only a short action title, the paragraph, and a thin progress line. The closing comparison shows the original and revision side by side on desktop and stacked on mobile, with only Before and After labels. The desktop canvas is 1120 × 480; the mobile canvas is 640 × 850.

## Files

- `desktop.gif` / `mobile.gif`: README animations, 24 seconds at 12.5 frames per second.
- `desktop-still.svg` / `mobile-still.svg`: editable, accessible static views of the closing comparison.
- [source.html](source.html): self-contained animation source. Download and open it in a browser to play, pause, seek, or switch layouts. It makes no network requests.

The README displays a GIF by default. A single width query selects the mobile composition on narrow screens; clients that ignore the query still receive the desktop GIF. A separate link below the animation opens a static SVG.

## Rebuild the artwork

These are optional development tools. Using the writing skill requires none of them.

Install Playwright for Node.js and Pillow for Python in your development environment, then run from the repository root:

```sh
node scripts/render-workflow.cjs
python scripts/encode-workflow.py
python scripts/validate.py
```

Playwright needs a Chromium browser. Set `WORKFLOW_BROWSER` to an existing browser executable if needed, and `WORKFLOW_PLAYWRIGHT` to the installed module path if it is outside Node's normal search path. These are local build settings, not part of the writing workflow.

The renderer writes temporary frames and layout checks to the ignored `build/workflow/` folder. Use `--keyframes-only` to check the composition before rendering every frame. The encoder uses one palette per GIF to keep the text and highlighting consistent. It verifies the duration after encoding.

Edit `DRAFT`, `STAGES`, `FINAL`, and `scenes` in the source to change the example or timing. Each entry in `STAGES` matches a move in the written example. Preserve the claims, conditions, and research progression as sentence boundaries change. The renderer exports timing metadata for the encoder.

The 24-second sequence gives 1 second to the input, 3 to explicit actions, 3 to moving the state beside its object, 4 to completing the interface, 4 to pairing the protocol, 3 to the closing result, 1 to the final paragraph, and 5 to the full Before/After comparison. Each revision takes 1.05 seconds to move into place; the result then stays visible for 1.5–2.5 seconds before the next step. Teal marks the relation being revised, rust marks removal, and green keeps attention on a retained condition or result. The final view removes the highlights for uninterrupted reading.

## Motion references

Public pages consulted on 2026-10-13:

| Reference | Principle used here |
|---|---|
| [Linear](https://linear.app/) | Keep a recognisable workspace on screen while attention moves to a local action. |
| [Zed](https://zed.dev/) | Use restrained framing and typography so the work itself remains the focal point. |
| [VHS](https://github.com/charmbracelet/vhs) | Show an operation, then hold its result long enough to read; make the demo reproducible from source. |

The paragraph, artwork, animation code, and timing are original. No screenshots, logos, footage, or code from these references are included.

GitHub lists GIF and SVG among its [supported image formats](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files).
