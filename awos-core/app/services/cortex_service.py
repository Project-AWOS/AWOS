"""
=========================================================
Module      : cortex_service.py

System      : AWOS

Component   : Services

Purpose
-------
Runs the complete CORTEX pipeline.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.cortex.analyzer import analyze_mission
from app.cortex.classifier import classify_mission
from app.cortex.reasoner import MissionReasoner
from app.cortex.planner import create_execution_plan

from app.models.planning import MissionPlan


def process_mission(
    mission: str,
) -> MissionPlan:
    """
    Execute the complete CORTEX pipeline.
    """

    analysis = analyze_mission(mission)

    classification = classify_mission(
        analysis
    )

    reasoning = MissionReasoner().reason(
        analysis,
        classification,
    )

    plan = create_execution_plan(
        reasoning
    )

    return plan
