# -*- coding: utf-8 -*-
"""Verification script for the final CEO suite."""
import re

files = [
    'FULCRUM_FINAL_CEO_BRIEFING.md',
    'FULCRUM_EXECUTIVE_EVIDENCE_APPENDIX.md',
    'FULCRUM_CEO_DECISION_SCORECARD.md'
]

banned = ['eli5', 'non-technical', 'dumb', 'anitha']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f'=== {fname} ===')
    for b in banned:
        count = text.lower().count(b)
        print(f'  Banned check "{b}": {count}')
    
    diagrams = re.findall(r'```mermaid(.*?)```', text, re.DOTALL)
    print(f'  Mermaid diagrams: {len(diagrams)}')
    for idx, d in enumerate(diagrams, 1):
        lines = [l.strip() for l in d.strip().split('\n') if l.strip()]
        first = lines[0] if lines else 'EMPTY'
        print(f'    Diagram {idx}: {first}')
        # Check edge labels for special chars
        edge_labels = re.findall(r'\|([^|]+)\|', d)
        bad = [l for l in edge_labels if any(c in l for c in ['(', ')', '/', ':', '"', '\''])]
        if bad:
            print(f'      WARNING bad edge labels: {bad}')

