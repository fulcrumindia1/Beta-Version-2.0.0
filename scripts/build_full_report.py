# -*- coding: utf-8 -*-
"""
Master Builder for the Comprehensive Fulcrum Alpha-to-Beta Development Value,
Cost and AI Feasibility Report.
Integrates Parts 1 through 8 and writes out the final Markdown report to:
DOCUMENTATION/FULCRUM_ALPHA_TO_BETA_DEVELOPMENT_VALUE_AND_COST_REPORT.md
"""

import os
import sys

# Add scripts directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from report_part1_intro import get_part1_text
from report_part2_diagrams import get_part2_text
from report_part3_feature_time import get_part3_text
from report_part4_ai_feasibility import get_part4_text
from report_part5_team_salaries import get_part5_text
from report_part6_monthly_costs import get_part6_text
from report_part7_build_costs_recommendations import get_part7_text
from report_part8_brutal_commercial_reality import get_part8_text

def build_report():
    print("Building comprehensive report with Section 24...")
    parts = [
        get_part1_text(),
        "\n---\n\n",
        get_part2_text(),
        "\n---\n\n",
        get_part3_text(),
        "\n---\n\n",
        get_part4_text(),
        "\n---\n\n",
        get_part5_text(),
        "\n---\n\n",
        get_part6_text(),
        "\n---\n\n",
        get_part7_text(),
        "\n---\n\n",
        get_part8_text()
    ]
    
    full_text = "".join(parts)
    
    # Validation checks
    print(f"Total characters: {len(full_text):,}")
    lines = full_text.split("\n")
    print(f"Total lines: {len(lines):,}")
    words = full_text.split()
    print(f"Total words: {len(words):,}")
    
    # Check for all diagrams
    diagram_count = full_text.count("```mermaid")
    print(f"Mermaid diagrams found: {diagram_count}")
    
    # Check target path
    doc_dir = os.path.join(os.path.dirname(current_dir), "DOCUMENTATION")
    os.makedirs(doc_dir, exist_ok=True)
    target_path = os.path.join(doc_dir, "FULCRUM_ALPHA_TO_BETA_DEVELOPMENT_VALUE_AND_COST_REPORT.md")
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_text)
        
    print(f"SUCCESS: Written to {target_path}")
    print(f"File size on disk: {os.path.getsize(target_path):,} bytes")

if __name__ == "__main__":
    build_report()
