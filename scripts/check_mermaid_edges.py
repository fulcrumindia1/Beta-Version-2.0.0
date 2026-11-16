# -*- coding: utf-8 -*-
"""Check edge labels in Mermaid diagrams."""
import re

with open('FULCRUM_CEO_BRIEFING_DIAGRAMS.md', 'r', encoding='utf-8') as f:
    text = f.read()

diagrams = re.findall(r'```mermaid(.*?)```', text, re.DOTALL)
for idx, d in enumerate(diagrams, 1):
    edge_labels = re.findall(r'\|([^|]+)\|', d)
    bad = [l for l in edge_labels if any(c in l for c in ['(', ')', '/', ':', '"', '\''])]
    if bad:
        print(f"Diagram {idx} has edge labels with special characters:")
        for b in bad:
            print(f"   |{b}|")

