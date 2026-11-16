# -*- coding: utf-8 -*-
"""
Master Builder for FULCRUM_BETA_FEASIBILITY_REPORT.md
Combines Parts 1-4, 5-8, 9-12, and 13-15 into a single authoritative report.
Target Path: DOCUMENTATION/FULCRUM_BETA_FEASIBILITY_REPORT.md
"""

import os
import sys

# Ensure scripts directory is in path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from feasibility_part1_to_4 import get_part1_to_4_text
from feasibility_part5_to_8 import get_part5_to_8_text
from feasibility_part9_to_12 import get_part9_to_12_text
from feasibility_part13_to_15 import get_part13_to_15_text

def build_full_feasibility_report():
    print("Assembling FULCRUM_BETA_FEASIBILITY_REPORT.md...")
    
    parts = [
        get_part1_to_4_text(),
        "\n\n",
        get_part5_to_8_text(),
        "\n\n",
        get_part9_to_12_text(),
        "\n\n",
        get_part13_to_15_text()
    ]
    
    full_text = "".join(parts)
    
    # Statistical analysis
    char_count = len(full_text)
    line_count = len(full_text.split("\n"))
    word_count = len(full_text.split())
    mermaid_count = full_text.count("```mermaid")
    table_count = full_text.count("| :---")
    
    print("=" * 60)
    print("REPORT METRICS & QUALITY AUDIT:")
    print(f"Total Characters: {char_count:,}")
    print(f"Total Lines:      {line_count:,}")
    print(f"Total Words:      {word_count:,}")
    print(f"Mermaid Diagrams: {mermaid_count}")
    print(f"Markdown Tables:  {table_count}")
    print("=" * 60)
    
    # Target directory
    target_dir = os.path.join(os.path.dirname(current_dir), "DOCUMENTATION")
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "FULCRUM_BETA_FEASIBILITY_REPORT.md")
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(full_text)
        
    print(f"SUCCESS: Successfully generated {target_file}")
    print(f"Disk file size: {os.path.getsize(target_file):,} bytes")

if __name__ == "__main__":
    build_full_feasibility_report()
