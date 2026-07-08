"""
=========================================================
Module      : execution_service.py

System      : AWOS

Component   : Services

Purpose
-------
Executes missions through the AWOS LangGraph workflow.

Workflow
--------
Mission
    ↓
Analyzer
    ↓
Classifier
    ↓
Reasoner
    ↓
Planner
    ↓
CEO
    ↓
Research
    ↓
Engineer
    ↓
QA
    ↓
Approval (if required)
    ↓
Mission Result

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.graph.workflow import build_workflow
from app.graph.state import MissionState
from app.models.planning import MissionPlan


# Build the workflow once during application startup
workflow = build_workflow()


def execute_mission(
    mission: str,
) -> MissionPlan:
    """
    Execute a mission using the complete AWOS workflow.

    Parameters
    ----------
    mission : str
        User mission or request.

    Returns
    -------
    MissionPlan
        Final execution plan produced by the workflow.
    """

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

    final_state = workflow.invoke(state)

    return final_state["plan"]
