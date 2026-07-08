"""
=========================================================
Module      : workflow.py

System      : AWOS

Component   : LangGraph

Purpose
-------
Defines the LangGraph workflow for AWOS.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from langgraph.graph import StateGraph, START, END

from app.graph.state import MissionState

from app.graph.nodes import (
    analyzer_node,
    classifier_node,
    reasoner_node,
    planner_node,
)


def build_workflow():

    graph = StateGraph(MissionState)

    graph.add_node("analyzer", analyzer_node)
    graph.add_node("classifier", classifier_node)
    graph.add_node("reasoner", reasoner_node)
    graph.add_node("planner", planner_node)

    graph.add_edge(START, "analyzer")
    graph.add_edge("analyzer", "classifier")
    graph.add_edge("classifier", "reasoner")
    graph.add_edge("reasoner", "planner")
    graph.add_edge("planner", END)

    return graph.compile()