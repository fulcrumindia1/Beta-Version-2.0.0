# -*- coding: utf-8 -*-
"""Verification script for CEO Briefing deliverables."""
import re

with open('FULCRUM_CEO_BRIEFING_360.md', 'r', encoding='utf-8') as f:
    text360 = f.read()

with open('FULCRUM_CEO_BRIEFING_DIAGRAMS.md', 'r', encoding='utf-8') as f:
    textDiag = f.read()

banned = ['eli5', 'non-technical', 'dumb', 'anitha']
for b in banned:
    c360 = text360.lower().count(b)
    cDiag = textDiag.lower().count(b)
    print(f'Banned word check "{b}": in 360={c360}, in Diag={cDiag}')

diagrams = re.findall(r'```mermaid(.*?)```', textDiag, re.DOTALL)
print(f'Total diagrams in FULCRUM_CEO_BRIEFING_DIAGRAMS.md: {len(diagrams)}')
for idx, d in enumerate(diagrams, 1):
    first_line = [l.strip() for l in d.strip().split('\n') if l.strip()][0]
    print(f'  Diagram {idx}: {first_line}')

