"""
=========================================================
Module      : ceo.py

System      : AWOS

Component   : CEO Agent

Purpose
-------
Makes high-level execution decisions
for a mission.

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
from app.models.decision import AgentDecision


class CEOAgent:
    """
    Chief Executive Officer Agent.

    Temporary mock implementation.
    """

    def decide(
        self,
        analysis: MissionAnalysis,
        classification: MissionClassification,
    ) -> AgentDecision:

        return AgentDecision(
            summary="Mission approved by CEO.",

            use_research=True,
            use_engineer=True,
            use_qa=True,

            requires_approval=False,

            tools=[
                "GitHub MCP",
            ],
        )