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
Genesis v2.0
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

You are NOT responsible for solving the mission.

Your responsibilities are:

1. Decide whether the Research Agent is required.
2. Decide whether the Engineer Agent is required.
3. Decide whether the QA Agent is required.
4. Decide whether human approval is required.
5. Decide which MCP tools should be used.
6. Explain WHY you made these decisions.

=================================================
MISSION ANALYSIS
=================================================

{analysis.model_dump_json(indent=2)}

=================================================
MISSION CLASSIFICATION
=================================================

{classification.model_dump_json(indent=2)}

=================================================
INSTRUCTIONS
=================================================

Return ONLY valid JSON.

Do NOT include markdown.

Do NOT include explanations.

Return exactly the following fields:

- summary (string)
- use_research (boolean)
- use_engineer (boolean)
- use_qa (boolean)
- requires_approval (boolean)
- tools (array of strings)
- reason (string)

The "reason" field must briefly explain why the selected agents and tools are needed.

=================================================
EXAMPLE
=================================================

{{
    "summary": "Mission approved.",

    "use_research": true,

    "use_engineer": true,

    "use_qa": false,

    "requires_approval": false,

    "tools": [
        "GitHub MCP"
    ],

    "reason": "Research is required to gather implementation details before engineering begins."
}}
"""