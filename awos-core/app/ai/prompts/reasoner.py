"""
=========================================================
Module      : reasoner.py

System      : AWOS

Component   : Reasoner Prompt

Purpose
-------
Builds the prompt used by the Mission Reasoner.

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


def build_reasoner_prompt(
    analysis: MissionAnalysis,
    classification: MissionClassification,
) -> str:
    """
    Build the Gemini reasoning prompt.
    """

    return f"""
You are the Chief Reasoning Engine of AWOS.

Your responsibility is to determine the best execution
strategy for the mission.

Mission Analysis

Objective:
{analysis.objective}

Priority:
{analysis.priority}

Complexity:
{analysis.complexity}

Mission Classification

Category:
{classification.category}

Requires AI:
{classification.requires_ai}

Requires Research:
{classification.requires_research}

Return ONLY valid JSON.

Example:

{{
    "summary": "...",
    "approach": "...",
    "required_agents": [
        "Research",
        "Engineer",
        "QA"
    ],
    "estimated_steps": 5,
    "risk": "Low"
}}
"""