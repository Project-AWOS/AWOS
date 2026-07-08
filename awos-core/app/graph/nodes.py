"""
=========================================================
Module      : nodes.py

System      : AWOS

Component   : LangGraph

Purpose
-------
Defines the LangGraph nodes that execute the
AWOS CORTEX pipeline.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.graph.state import MissionState

from app.cortex.analyzer import analyze_mission
from app.cortex.classifier import classify_mission
from app.cortex.reasoner import MissionReasoner
from app.cortex.planner import create_execution_plan


def analyzer_node(state: MissionState) -> MissionState:
    """
    Run the mission analyzer.
    """

    state["analysis"] = analyze_mission(state["mission"])
    return state


def classifier_node(state: MissionState) -> MissionState:
    """
    Run the mission classifier.
    """

    state["classification"] = classify_mission(
        state["analysis"]
    )

    return state


def reasoner_node(state: MissionState) -> MissionState:
    """
    Run Gemini reasoning.
    """

    state["reasoning"] = MissionReasoner().reason(
        state["analysis"],
        state["classification"],
    )

    return state


def planner_node(state: MissionState) -> MissionState:
    """
    Create the execution plan.
    """

    state["plan"] = create_execution_plan(
        state["reasoning"]
    )

    return state