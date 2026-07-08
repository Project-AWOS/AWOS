"""
=========================================================
Module      : ceo.py

System      : AWOS

Component   : CEO Prompt

Purpose
-------
Prompt used by the CEO Agent to decide how a
mission should be executed.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.models.analysis import MissionAnalysis
from app.models.classification import MissionClassification


def build_ceo_prompt(
    analysis: MissionAnalysis,
    classification: MissionClassification,
) -> str:
    """
    Build the CEO prompt.
    """

    return f"""
You are the CEO of AWOS (Autonomous Workforce Operating System).

Your responsibility is NOT to solve the mission.

Your responsibility is to decide:

1. Which agents are required.
2. Whether human approval is needed.
3. Which tools should be used.

Mission Analysis

{analysis.model_dump_json(indent=2)}

Mission Classification

{classification.model_dump_json(indent=2)}

Return ONLY valid JSON.

Example:

{{
    "summary": "...",

    "use_research": true,
    "use_engineer": true,
    "use_qa": true,

    "requires_approval": false,

    "tools": [
        "GitHub MCP"
    ]
}}
"""