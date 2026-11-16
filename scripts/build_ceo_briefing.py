# -*- coding: utf-8 -*-
"""
Master Builder for CEO Briefing Documents:
1. FULCRUM_CEO_BRIEFING_360.md
2. FULCRUM_CEO_BRIEFING_DIAGRAMS.md
"""

import os
import sys

# Ensure current scripts directory is on path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from ceo_briefing_part1 import get_part1_text
from ceo_briefing_part2 import get_part2_text
from ceo_briefing_part3 import get_part3_text
from ceo_briefing_part4 import get_part4_text
from ceo_briefing_part5 import get_part5_text
from ceo_briefing_diagrams import get_diagrams_text

def build_all_ceo_documents():
    workspace_dir = os.path.dirname(current_dir)
    docs_dir = os.path.join(workspace_dir, "DOCUMENTATION")
    os.makedirs(docs_dir, exist_ok=True)
    
    print("=" * 60)
    print("BUILDING CEO BRIEFING DOCUMENTS")
    print("=" * 60)
    
    # 1. Assemble FULCRUM_CEO_BRIEFING_360.md
    print("Assembling FULCRUM_CEO_BRIEFING_360.md...")
    main_report_parts = [
        get_part1_text(),
        "\n\n",
        get_part2_text(),
        "\n\n",
        get_part3_text(),
        "\n\n",
        get_part4_text(),
        "\n\n",
        get_part5_text()
    ]
    main_report_text = "".join(main_report_parts)
    
    # Paths for main report
    root_main_path = os.path.join(workspace_dir, "FULCRUM_CEO_BRIEFING_360.md")
    docs_main_path = os.path.join(docs_dir, "FULCRUM_CEO_BRIEFING_360.md")
    
    with open(root_main_path, "w", encoding="utf-8") as f:
        f.write(main_report_text)
    with open(docs_main_path, "w", encoding="utf-8") as f:
        f.write(main_report_text)
        
    print(f"SUCCESS: Written {root_main_path} ({len(main_report_text):,} chars, {len(main_report_text.split()):,} words)")
    print(f"SUCCESS: Synced copy to {docs_main_path}")
    
    # 2. Assemble FULCRUM_CEO_BRIEFING_DIAGRAMS.md
    print("\nAssembling FULCRUM_CEO_BRIEFING_DIAGRAMS.md...")
    diagrams_text = get_diagrams_text()
    
    root_diagrams_path = os.path.join(workspace_dir, "FULCRUM_CEO_BRIEFING_DIAGRAMS.md")
    docs_diagrams_path = os.path.join(docs_dir, "FULCRUM_CEO_BRIEFING_DIAGRAMS.md")
    
    with open(root_diagrams_path, "w", encoding="utf-8") as f:
        f.write(diagrams_text)
    with open(docs_diagrams_path, "w", encoding="utf-8") as f:
        f.write(diagrams_text)
        
    print(f"SUCCESS: Written {root_diagrams_path} ({len(diagrams_text):,} chars, {len(diagrams_text.split()):,} words)")
    print(f"SUCCESS: Synced copy to {docs_diagrams_path}")
    
    # 3. Validation Audit
    diagram_count = diagrams_text.count("```mermaid")
    print("\n" + "=" * 60)
    print("QUALITY AUDIT SUMMARY:")
    print(f"Main Report Words:     {len(main_report_text.split()):,}")
    print(f"Main Report Lines:     {len(main_report_text.splitlines()):,}")
    print(f"Diagrams File Words:   {len(diagrams_text.split()):,}")
    print(f"Diagrams Count:        {diagram_count} of 12 required")
    print("=" * 60)

if __name__ == "__main__":
    build_all_ceo_documents()
