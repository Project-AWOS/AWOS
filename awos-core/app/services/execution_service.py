"""
=========================================================
Module      : execution_service.py

System      : AWOS

Component   : Services

Purpose
-------
Executes missions through the AWOS LangGraph workflow.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.graph.workflow import build_workflow
from app.models.planning import MissionPlan


workflow = build_workflow()


def execute_mission(
    mission: str,
) -> MissionPlan:
    """
    Execute a mission through the LangGraph workflow.
    """

    state = {
    "mission": mission,

    "analysis": None,
    "classification": None,
    "reasoning": None,

    "decision": None,

    "research": None,
    "engineering": None,
    "qa": None,
    "approval": None,

    "plan": None,
}

    result = workflow.invoke(state)

    return result["plan"]