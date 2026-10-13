#!/usr/bin/env python3
"""Offline structural checks. These do not measure writing quality or equivalence."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'revise-research-writing'
REFS = SKILL / 'references'
ERRORS: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f'{path.relative_to(ROOT)}: {exc}')
        return {}


def anchors(text: str) -> set[str]:
    found = set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
    seen: Counter[str] = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        heading = re.sub(r'<[^>]+>', '', heading).lower()
        slug = re.sub(r'[^\w\- ]', '', heading, flags=re.UNICODE).replace(' ', '-')
        index = seen[slug]
        seen[slug] += 1
        found.add(f'{slug}-{index}' if index else slug)
    return found


def main() -> int:
    entry = SKILL / 'SKILL.md'
    check(entry.is_file(), 'Missing SKILL.md')
    text = entry.read_text(encoding='utf-8') if entry.is_file() else ''
    check(text.startswith('---\n'), 'SKILL.md needs YAML frontmatter')
    header = text.split('---', 2)[1] if text.count('---') >= 2 else ''
    check(bool(re.search(r'^name: revise-research-writing$', header, re.M)), 'Unexpected skill name')
    check(bool(re.search(r'^description: \S.+$', header, re.M)), 'Missing description')
    check(len(text.splitlines()) <= 100, 'Entrypoint grew beyond the intended small router')
    for required in ['LICENSE', 'ATTRIBUTION.md', 'README.md', 'CHANGELOG.md',
                     'examples/before-after.md', 'examples/acceptance-cases.json']:
        check((ROOT / required).is_file(), f'Missing {required}')

    corpus = read_json(REFS / 'corpus-manifest.json')
    papers = corpus.get('papers', [])
    ids = {p.get('id') for p in papers}
    expected = {f'{group}{i:02d}' for group in ('H', 'X') for i in range(1, 16)}
    check(len(papers) == 30 and ids == expected, 'Expected 30 unique H/X paper records')
    counts = Counter(p.get('target_author') for p in papers)
    check(counts == {'Kaiming He': 15, 'Saining Xie': 15}, 'Author-group counts differ from 15 + 15')
    for paper in papers:
        pid = paper.get('id')
        for key in ['title', 'authors', 'version_note', 'observation_locations']:
            check(bool(paper.get(key)), f'{pid}: missing {key}')
        for key in ['official_record_url', 'read_version_url']:
            check(str(paper.get(key, '')).startswith('https://'), f'{pid}: invalid {key}')
        check(paper.get('authors', [None])[-1] == paper.get('target_author'),
              f'{pid}: selected target author is not last-listed')
        check('reading_coverage' not in paper, f'{pid}: internal process log must not be packaged')

    index = read_json(REFS / 'observation-index.json').get('papers', {})
    check(set(index) == expected, 'Observation index does not match corpus IDs')
    dimension_ids = {f'D{i}' for i in range(1, 16)}
    layer_ids = {f'L{i}' for i in range(1, 9)}
    observations = 0
    for pid, record in index.items():
        dims = record.get('dimensions', {})
        check(bool(record.get('source_id')), f'{pid}: missing stable source ID')
        check(set(dims) == dimension_ids, f'{pid}: expected D1–D15')
        covered: set[str] = set()
        for dim, item in dims.items():
            observations += 1
            check(bool(item.get('location')), f'{pid}/{dim}: missing locator')
            layers = set(item.get('layers', []))
            check(bool(layers) and layers <= layer_ids, f'{pid}/{dim}: invalid layers')
            covered |= layers
        check(covered == layer_ids, f'{pid}: L1–L8 are not all represented')

    cards_text = (REFS / 'sentence-craft.md').read_text(encoding='utf-8')
    card_ids = re.findall(r'^## (S\d+) ', cards_text, re.M)
    check(card_ids == [f'S{i}' for i in range(1, 10)], 'Expected ordered S1–S9 cards')
    evidence_refs = []
    for card in re.split(r'^## S\d+ ', cards_text, flags=re.M)[1:]:
        check('**Keep**' in card, 'Each card needs a keep case')
        check('**等义核对**' in card, 'Each card needs a fidelity check')
        check('dimension-map.md' in card, 'Each card needs a D-dimension pointer')
        source = card.split('**源语境**', 1)[-1]
        evidence_refs.extend(re.findall(r'\[([HX]\d{2})\]', source))
    check(len(evidence_refs) == 24, f'Expected 24 direct card mechanisms, found {len(evidence_refs)}')
    check(len(set(evidence_refs)) == 17, 'Expected 17 distinct direct card sources')
    check(set(evidence_refs) <= expected, 'Unknown card source ID')

    examples = read_json(ROOT / 'examples' / 'acceptance-cases.json').get('cases', [])
    check(len(examples) == 8, 'Expected eight behavioral cases')
    check(len({e.get('id') for e in examples}) == len(examples), 'Duplicate example IDs')
    for example in examples:
        check(all(example.get(k) for k in ['id', 'purpose', 'request', 'input', 'invariants', 'failures', 'cards']),
              f'{example.get("id")}: incomplete example')
        check(set(example.get('cards', [])) <= set(card_ids), f'{example.get("id")}: unknown card')

    # Resolve Markdown and HTML links, including same-file fragments.
    link_count = 0
    external_urls: set[str] = set()
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts or path.relative_to(ROOT).parts[0] == 'build':
            continue
        content = path.read_text(encoding='utf-8')
        targets = re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)', content)
        targets += re.findall(r'(?:href|src|srcset)=[\"\']([^\"\']+)', content)
        for raw in targets:
            url = urlsplit(raw)
            if url.scheme in {'https', 'http', 'mailto'}:
                external_urls.add(raw)
                continue
            link_count += 1
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            check(dest.is_relative_to(ROOT), f'{path.relative_to(ROOT)}: link escapes repository: {raw}')
            check(dest.exists(), f'{path.relative_to(ROOT)}: missing link target: {raw}')
            if url.fragment and dest.is_file() and dest.suffix == '.md':
                check(unquote(url.fragment) in anchors(dest.read_text(encoding='utf-8')),
                      f'{path.relative_to(ROOT)}: missing anchor: {raw}')

    # Original homepage GIFs have editable sources and static SVG counterparts.
    allowed = {'.md', '.json', '.py', '.svg', '.yaml', '.yml'}
    animation_sizes = {
        'assets/workflow/desktop.gif': (1120, 480),
        'assets/workflow/mobile.gif': (640, 850),
    }
    artwork_sources = {'assets/workflow/source.html', 'scripts/render-workflow.cjs'}
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] == 'build':
            continue  # Local render frames are ignored build output.
        name = relative.as_posix()
        if name in animation_sizes:
            data = path.read_bytes()
            check(len(data) >= 10 and data[:6] in {b'GIF87a', b'GIF89a'}, f'{relative}: invalid GIF header')
            if len(data) >= 10:
                size = (int.from_bytes(data[6:8], 'little'), int.from_bytes(data[8:10], 'little'))
                check(size == animation_sizes[name], f'{relative}: unexpected GIF dimensions')
            check(len(data) <= 5 * 1024 * 1024, f'{relative}: GIF exceeds the artwork size budget')
            continue
        check(path.suffix in allowed or path.name in {'LICENSE', '.gitignore'} or name in artwork_sources,
              f'Unexpected artifact: {relative}')
        if path.name == 'validate.py':
            continue  # The scanner's patterns are not secrets or leaked paths.
        content = path.read_text(encoding='utf-8')
        check(not re.search(r'/(?:workspace|Users)/|/home/agent/|/root/\.codex/', content),
              f'{relative}: internal absolute path')
        check(not re.search(r'-----BEGIN [A-Z ]*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{24,}|sk-[A-Za-z0-9]{32,}', content),
              f'{relative}: possible credential')
        if path.suffix == '.svg':
            try:
                svg = ET.fromstring(content)
                check(svg.tag.endswith('svg'), f'{relative}: invalid SVG root')
                check(not re.search(r'<script|<foreignObject|https?://(?!www.w3.org)', content, re.I),
                      f'{relative}: active or external SVG content')
            except ET.ParseError as exc:
                ERRORS.append(f'{relative}: invalid SVG: {exc}')

    if ERRORS:
        for error in ERRORS:
            print(f'FAIL: {error}', file=sys.stderr)
        print(f'{len(ERRORS)} check(s) failed.', file=sys.stderr)
        return 1
    print('PASS: corpus IDs, author-group structure, dimension locators, and L1–L8 coverage.')
    print(f'PASS: {len(card_ids)} cards; {len(evidence_refs)} mechanisms from {len(set(evidence_refs))} papers; {len(examples)} behavioral cases.')
    print(f'PASS: {link_count} local links/anchors; package boundary and SVG checks.')
    print(f'NOTE: {len(external_urls)} external URLs found, not fetched by this offline validator.')
    print('NOTE: Static checks do not establish semantic equivalence, writing quality, or model performance.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
