"""Encode the optional homepage artwork. Requires Pillow; the skill itself does not."""
from pathlib import Path
import argparse, json, re
from PIL import Image, ImageColor

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--frames', type=Path, default=root / 'build' / 'workflow')
args = parser.parse_args()
report = []
settings = json.loads((args.frames / 'render-settings.json').read_text(encoding='utf-8'))
for layout in ('desktop', 'mobile'):
    paths = sorted((args.frames / layout / 'frames').glob('*.png'))
    if len(paths) != settings['frame_count']:
        raise SystemExit(f"{layout}: expected {settings['frame_count']} frames, found {len(paths)}")
    # One palette across the whole sequence keeps type and highlights consistent.
    samples = []
    for p in sorted((args.frames / layout).glob('key-*.png')):
        with Image.open(p) as im:
            samples.append(im.convert('RGB'))
    # Sample original pixels so smaller comparison text retains its edge colors.
    sheet = Image.new('RGB', (max(im.width for im in samples), sum(im.height for im in samples)), '#f4f1e9')
    y = 0
    for im in samples:
        sheet.paste(im, (0, y)); y += im.height
    palette = sheet.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    # Keep the exact ink and annotation colors available in the shared palette.
    source = (root / 'assets' / 'workflow' / 'source.html').read_text(encoding='utf-8')
    core = list(dict.fromkeys(re.findall(r"'(#[0-9a-fA-F]{6})'", source)))
    exact = [value for color in core for value in ImageColor.getrgb(color)]
    sampled = palette.getpalette()
    palette.putpalette(exact + sampled[len(exact):])
    frames = []
    for p in paths:
        with Image.open(p) as im:
            frames.append(im.convert('RGB').quantize(palette=palette, dither=Image.Dither.NONE))
    target = root / 'assets' / 'workflow' / (layout + '.gif')
    frames[0].save(target, save_all=True, append_images=frames[1:], duration=settings['frame_ms'],
                   loop=0, optimize=False, disposal=1, interlace=False)
    del frames
    with Image.open(target) as im:
        duration = 0
        for frame in range(im.n_frames):
            im.seek(frame); duration += im.info.get('duration', 0)
        assert duration == settings['duration_ms'], (layout, duration)
        report.append({'file':target.name, 'bytes':target.stat().st_size,
                       'dimensions':im.size, 'frames':im.n_frames, 'duration_ms':duration})
    print(json.dumps(report[-1]), flush=True)
(args.frames / 'gif-checks.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
