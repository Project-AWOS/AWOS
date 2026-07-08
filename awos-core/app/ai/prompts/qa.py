"""
=========================================================
Module      : qa.py

System      : AWOS

Component   : QA Prompt

Purpose
-------
Builds the prompt used by the QA Agent.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

def build_qa_prompt(mission: str) -> str:
    """
    Build the QA Agent prompt.
    """

    return f"""
You are the QA Agent of AWOS.

Your responsibilities are:

1. Review the execution.
2. Identify risks.
3. Validate quality.
4. Decide whether the mission is ready.

Mission

{mission}

Return ONLY valid JSON.

Example:

{{
    "passed": true,
    "score": 95,
    "feedback": [
        "...",
        "...",
        "..."
    ]
}}
"""