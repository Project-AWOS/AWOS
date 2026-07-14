"""
=========================================================
Module      : decision.py

System      : AWOS

Component   : Models

Purpose
-------
Stores the decision made by the CEO Agent
after reviewing the mission.

Author
------
Project AWOS Team

Version
-------
Genesis v2.0
=========================================================
"""

from pydantic import BaseModel, Field


class AgentDecision(BaseModel):
    """
    Decision returned by the CEO Agent.
    """

    # Mission summary
    summary: str

    # Which agents should execute
    use_research: bool = False
    use_engineer: bool = False
    use_qa: bool = False

    # Human approval required?
    requires_approval: bool = False

    # MCP tools expected to be used
    tools: list[str] = Field(default_factory=list)

    # Why CEO made this decision
    reason: str
