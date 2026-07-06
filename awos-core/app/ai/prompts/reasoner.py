"""
=========================================================
Module      : reasoner.py

System      : AWOS

Component   : AI Prompt

Purpose
-------
Prompt template for the CORTEX Reasoner.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""


def build_reasoner_prompt(
    analysis,
    classification,
) -> str:
    """
    Build the prompt sent to Gemini.
    """

    return f"""
You are the CORTEX Brain of AWOS.

Your task is to determine how AWOS should execute this mission.

MISSION ANALYSIS

Original Mission:
{analysis.original_text}

Normalized Mission:
{analysis.normalized_text}

Keywords:
{analysis.keywords}

Word Count:
{analysis.word_count}

Sentence Count:
{analysis.sentence_count}

----------------------------------------

MISSION CLASSIFICATION

Domain:
{classification.domain}

Category:
{classification.category}

Complexity:
{classification.complexity}

----------------------------------------

Return ONLY valid JSON.

Use exactly this schema.

{{
    "summary": "...",

    "required_agents": [
        "CEO",
        "Research",
        "Engineer",
        "QA"
    ],

    "required_tools": [
        "GitHub MCP"
    ],

    "execution_strategy": [
        "...",
        "...",
        "..."
    ],

    "risks": [
        "...",
        "..."
    ],

    "estimated_complexity": "Low | Medium | High"
}}
"""
"""
=========================================================
Module      : reasoner.py

System      : AWOS

Component   : AI Prompt

Purpose
-------
Prompt template for the CORTEX Reasoner.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""


def build_reasoner_prompt(
    analysis,
    classification,
) -> str:
    """
    Build the prompt sent to Gemini.
    """

    return f"""
You are the CORTEX Brain of AWOS.

Your task is to determine how AWOS should execute this mission.

MISSION ANALYSIS

Original Mission:
{analysis.original_text}

Normalized Mission:
{analysis.normalized_text}

Keywords:
{analysis.keywords}

Word Count:
{analysis.word_count}

Sentence Count:
{analysis.sentence_count}

----------------------------------------

MISSION CLASSIFICATION

Domain:
{classification.domain}

Category:
{classification.category}

Complexity:
{classification.complexity}

----------------------------------------

Return ONLY valid JSON.

Use exactly this schema.

{{
    "summary": "...",

    "required_agents": [
        "CEO",
        "Research",
        "Engineer",
        "QA"
    ],

    "required_tools": [
        "GitHub MCP"
    ],

    "execution_strategy": [
        "...",
        "...",
        "..."
    ],

    "risks": [
        "...",
        "..."
    ],

    "estimated_complexity": "Low | Medium | High"
}}
"""
