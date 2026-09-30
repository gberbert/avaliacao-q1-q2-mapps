#!/usr/bin/env python3
"""fix_fstrings.py
Substitui chaves simples { e } por {{ e }} dentro dos blocos de CSS e JS
adicionados aos arquivos build_rich_reef.py e update_i18n.py.
"""

def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Seção CSS do calc
    # Procurar bloco entre "/* Botón y Callout de Memoria de Cálculo */" e "/* Slide Navigation Modal"
    css_pattern = re.compile(r'(/\* Botón y Callout de Memoria de Cálculo \*/.*?)(/\* Slide Navigation Modal)', re.DOTALL)
    m_css = css_pattern.search(content)
    if m_css:
        raw_css = m_css.group(1)
        # Normalizar: se já tem {{ deixa, se tem { substitui
        fixed_css = raw_css.replace('{{', '{').replace('}}', '}').replace('{', '{{').replace('}', '}}')
        content = content[:m_css.start(1)] + fixed_css + content[m_css.end(1):]

    # Seção JS do calc
    js_pattern = re.compile(r'(// Calculation Memory Modal Logic.*?)(function (?:openImageModal|renderDrawerList))', re.DOTALL)
    m_js = js_pattern.search(content)
    if m_js:
        raw_js = m_js.group(1)
        fixed_js = raw_js.replace('{{', '{').replace('}}', '}').replace('{', '{{').replace('}', '}}')
        content = content[:m_js.start(1)] + fixed_js + content[m_js.end(1):]

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {path}")

import re
fix_file("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/build_rich_reef.py")
fix_file("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/update_i18n.py")
