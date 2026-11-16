# -*- coding: utf-8 -*-
"""
Master Builder for the Final Consolidated CEO Briefing Suite
Generates:
1. FULCRUM_FINAL_CEO_BRIEFING.md
2. FULCRUM_EXECUTIVE_EVIDENCE_APPENDIX.md
3. FULCRUM_CEO_DECISION_SCORECARD.md
And harmonizes FULCRUM_CEO_BRIEFING_360.md and FULCRUM_CEO_BRIEFING_DIAGRAMS.md
"""

import os
import sys

# Ensure scripts dir is in path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from final_briefing_main import get_final_ceo_briefing_text
from final_briefing_appendix import get_final_appendix_text
from final_briefing_scorecard import get_final_scorecard_text

def build_all_final_documents():
    workspace_dir = os.path.dirname(current_dir)
    docs_dir = os.path.join(workspace_dir, "DOCUMENTATION")
    os.makedirs(docs_dir, exist_ok=True)
    
    print("=" * 65)
    print("BUILDING FINAL CONSOLIDATED CEO BRIEFING SUITE")
    print("=" * 65)
    
    # 1. Main CEO Briefing
    print("\n1. Generating FULCRUM_FINAL_CEO_BRIEFING.md...")
    main_text = get_final_ceo_briefing_text()
    root_main = os.path.join(workspace_dir, "FULCRUM_FINAL_CEO_BRIEFING.md")
    docs_main = os.path.join(docs_dir, "FULCRUM_FINAL_CEO_BRIEFING.md")
    with open(root_main, "w", encoding="utf-8") as f:
        f.write(main_text)
    with open(docs_main, "w", encoding="utf-8") as f:
        f.write(main_text)
    print(f"   SUCCESS: {root_main} ({len(main_text):,} chars, {len(main_text.split()):,} words)")
    
    # Also harmonize FULCRUM_CEO_BRIEFING_360.md so it mirrors this master version
    root_360 = os.path.join(workspace_dir, "FULCRUM_CEO_BRIEFING_360.md")
    docs_360 = os.path.join(docs_dir, "FULCRUM_CEO_BRIEFING_360.md")
    with open(root_360, "w", encoding="utf-8") as f:
        f.write(main_text)
    with open(docs_360, "w", encoding="utf-8") as f:
        f.write(main_text)
    print(f"   SUCCESS: Harmonized FULCRUM_CEO_BRIEFING_360.md")
    
    # 2. Executive Evidence Appendix
    print("\n2. Generating FULCRUM_EXECUTIVE_EVIDENCE_APPENDIX.md...")
    app_text = get_final_appendix_text()
    root_app = os.path.join(workspace_dir, "FULCRUM_EXECUTIVE_EVIDENCE_APPENDIX.md")
    docs_app = os.path.join(docs_dir, "FULCRUM_EXECUTIVE_EVIDENCE_APPENDIX.md")
    with open(root_app, "w", encoding="utf-8") as f:
        f.write(app_text)
    with open(docs_app, "w", encoding="utf-8") as f:
        f.write(app_text)
    print(f"   SUCCESS: {root_app} ({len(app_text):,} chars, {len(app_text.split()):,} words)")
    
    # Also harmonize FULCRUM_CEO_BRIEFING_DIAGRAMS.md so it mirrors this appendix
    root_diag = os.path.join(workspace_dir, "FULCRUM_CEO_BRIEFING_DIAGRAMS.md")
    docs_diag = os.path.join(docs_dir, "FULCRUM_CEO_BRIEFING_DIAGRAMS.md")
    with open(root_diag, "w", encoding="utf-8") as f:
        f.write(app_text)
    with open(docs_diag, "w", encoding="utf-8") as f:
        f.write(app_text)
    print(f"   SUCCESS: Harmonized FULCRUM_CEO_BRIEFING_DIAGRAMS.md")
    
    # 3. CEO Decision Scorecard
    print("\n3. Generating FULCRUM_CEO_DECISION_SCORECARD.md...")
    score_text = get_final_scorecard_text()
    root_score = os.path.join(workspace_dir, "FULCRUM_CEO_DECISION_SCORECARD.md")
    docs_score = os.path.join(docs_dir, "FULCRUM_CEO_DECISION_SCORECARD.md")
    with open(root_score, "w", encoding="utf-8") as f:
        f.write(score_text)
    with open(docs_score, "w", encoding="utf-8") as f:
        f.write(score_text)
    print(f"   SUCCESS: {root_score} ({len(score_text):,} chars, {len(score_text.split()):,} words)")
    
    # 4. Statistical Summary
    print("\n" + "=" * 65)
    print("FINAL DELIVERY AUDIT:")
    print(f"Main Briefing:        {len(main_text.split()):,} words, {main_text.count('```mermaid')} diagrams")
    print(f"Evidence Appendix:    {len(app_text.split()):,} words, {app_text.count('```mermaid')} diagrams")
    print(f"Decision Scorecard:   {len(score_text.split()):,} words")
    print("=" * 65)

if __name__ == "__main__":
    build_all_final_documents()
