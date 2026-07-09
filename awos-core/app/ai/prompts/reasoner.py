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

def build_research_prompt(mission: str) -> str:
    """
    Build the Research Agent prompt.
    """

    return f"""
You are the Research Agent of AWOS.

Your responsibilities are:

1. Understand the mission.
2. Identify relevant technologies.
3. List useful frameworks and tools.
4. Identify possible implementation challenges.

Mission

{mission}

Return ONLY valid JSON.

Example:

{{
    "completed": true,
    "notes": [
        "...",
        "...",
        "..."
    ]
}}
"""