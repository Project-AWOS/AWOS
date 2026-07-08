"""
=========================================================
Module      : execution_service.py

System      : AWOS

Component   : Services

Purpose
-------
Executes missions through the AWOS LangGraph workflow.
=========================================================
"""

from app.graph.workflow import build_workflow
from app.graph.state import MissionState
from app.models.planning import MissionPlan


workflow = build_workflow()


async def execute_mission(
    mission: str,
) -> MissionPlan:

    state: MissionState = {
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

    result = await workflow.ainvoke(state)

    return result["plan"]
