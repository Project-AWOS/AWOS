"""
=========================================================
Module      : reasoning.py

System      : AWOS

Component   : Models

Purpose
-------
Defines the structured reasoning generated
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
    Structured reasoning produced by the
    CORTEX Reasoner.

    This model acts as the bridge between
    AI reasoning and workflow planning.
    """

    summary: str = Field(
        ...,
        description="Short summary of the mission reasoning."
    )

    required_agents: list[str] = Field(
        default_factory=list,
        description="Agents required to complete the mission."
    )

    required_tools: list[str] = Field(
        default_factory=list,
        description="External tools needed for execution."
    )

    execution_strategy: list[str] = Field(
        default_factory=list,
        description="Ordered high-level execution steps."
    )

    risks: list[str] = Field(
        default_factory=list,
        description="Potential risks identified by the AI."
    )

    estimated_complexity: str = Field(
        ...,
        description="AI estimated execution complexity."
    )
