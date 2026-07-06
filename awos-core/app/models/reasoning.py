"""
=========================================================
Module      : reasoning.py

System      : AWOS

Component   : Models

Purpose
-------
Defines the AI reasoning output generated
by the CORTEX Reasoner.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from pydantic import BaseModel, Field


class MissionReasoning(BaseModel):
    """
    Represents the structured reasoning
    produced by Gemini.
    """

    summary: str

    required_agents: list[str] = Field(default_factory=list)

    required_tools: list[str] = Field(default_factory=list)

    execution_strategy: list[str] = Field(default_factory=list)

    risks: list[str] = Field(default_factory=list)

    estimated_complexity: str