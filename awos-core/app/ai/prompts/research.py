"""
=========================================================
Module      : research.py

System      : AWOS

Component   : Research Prompt

Purpose
-------
Builds the prompt used by the Research Agent.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

def build_research_prompt(
    mission: str,
) -> str:
    """
    Build the Research Agent prompt.
    """

    return f"""
You are the Research Agent of AWOS.

Your job is to investigate the mission before
engineering begins.

Responsibilities
----------------
1. Understand the mission.
2. Identify technologies required.
3. Suggest frameworks and libraries.
4. Identify risks and dependencies.
5. Recommend best practices.

Mission
-------
{mission}

Return ONLY valid JSON.

Example:

{{
    "completed": true,
    "notes": [
        "FastAPI is suitable for backend APIs.",
        "Docker should be used for deployment.",
        "A relational database is recommended."
    ]
}}
"""