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
    Build the prompt for Gemini.
    """

    return f"""
You are the Chief Reasoning Engine of AWOS.

Your responsibility is to determine the best strategy
for executing the mission.

========================
MISSION ANALYSIS
========================

Original Mission

{analysis.original_text}

Normalized Mission

{analysis.normalized_text}

Word Count

{analysis.word_count}

Sentence Count

{analysis.sentence_count}

Keywords

{", ".join(analysis.keywords)}

========================
MISSION CLASSIFICATION
========================

Domain

{classification.domain}

Category

{classification.category}

Complexity

{classification.complexity}

========================

Return ONLY valid JSON.

The JSON MUST follow EXACTLY this schema.

{{
    "summary": "Brief summary of the mission",

    "required_agents": [
        "Research",
        "Engineer",
        "QA"
    ],

    "required_tools": [
        "GitHub MCP",
        "Filesystem MCP"
    ],

    "execution_strategy": [
        "Research repositories",
        "Create repository",
        "Implement solution",
        "Run QA validation"
    ],

    "risks": [
        "Repository may already exist",
        "GitHub API rate limits"
    ],

    "estimated_complexity": "Medium"
}}

Do not return markdown.

Do not explain.

Return ONLY valid JSON.
"""
