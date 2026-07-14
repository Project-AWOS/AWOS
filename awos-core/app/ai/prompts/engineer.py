"""
=========================================================
Module      : engineer.py

System      : AWOS

Component   : Engineer Prompt

Purpose
-------
Builds the prompt used by the Engineer Agent.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

def build_engineer_prompt(mission: str) -> str:
    """
    Build the Engineer Agent prompt.
    """

    return f"""
You are the Engineer Agent of AWOS.

Your responsibilities are:

1. Break the mission into engineering tasks.
2. Recommend implementation steps.
3. Suggest project structure.
4. Identify required technologies.

Mission

{mission}

Return ONLY valid JSON.

Example:

{{
    "completed": true,
    "actions": [
        "...",
        "...",
        "..."
    ]
}}
"""