#!/usr/bin/env python3
"""Genera FlowLab.html: un unico file stand-alone (font inclusi).

FlowLab — Prof.ssa Veronica Rossano (Gruppo di ricerca TELL), Dipartimento di Informatica,
Università degli Studi di Bari, con il supporto di Claude Code. Licenza CC BY-NC-SA 4.0.
"""
import base64, json, pathlib
root = pathlib.Path(__file__).parent
src = root / 'src'
fonts = [
    ('OpenDyslexic', 400, 'opendyslexic-latin-400-normal.woff2'),
    ('OpenDyslexic', 700, 'opendyslexic-latin-700-normal.woff2'),
    ('Lexend', 400, 'lexend-latin-400-normal.woff2'),
    ('Lexend', 700, 'lexend-latin-600-normal.woff2'),
    ('Atkinson Hyperlegible', 400, 'atkinson-hyperlegible-latin-400-normal.woff2'),
    ('Atkinson Hyperlegible', 700, 'atkinson-hyperlegible-latin-700-normal.woff2'),
]
fd = [{'family': f, 'weight': w, 'data': 'data:font/woff2;base64,' + base64.b64encode((root / 'fonts' / n).read_bytes()).decode()} for f, w, n in fonts]
js = 'const FONT_DATA = ' + json.dumps(fd) + ';\n'
for name in ['expr.js', 'model.js', 'runtime.js', 'layout.js', 'ui.js']:
    js += f'\n/* ---- {name} ---- */\n' + (src / name).read_text()
html = (src / 'index.html').read_text()
html = html.replace('/*CSS*/', (src / 'style.css').read_text()).replace('<!--DEFS-->', '')
html = html.replace('/*JS*/', js.replace('</script', '<\\/script'))
out = root / 'FlowLab.html'
out.write_text(html)
print(f'{out.name}: {out.stat().st_size // 1024} KB')
