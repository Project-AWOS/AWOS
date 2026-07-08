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
    ceo_node,
    research_node,
    engineer_node,
    qa_node,
    approval_node,
    planner_node,
)

def build_workflow():

    graph = StateGraph(MissionState)

    graph.add_node("analyzer", analyzer_node)
    graph.add_node("classifier", classifier_node)
    graph.add_node("reasoner", reasoner_node)
    graph.add_node("ceo", ceo_node)
    graph.add_node("research", research_node)
    graph.add_node("engineer", engineer_node)
    graph.add_node("qa", qa_node)
    graph.add_node("approval", approval_node)
    graph.add_node("planner", planner_node)

    graph.add_edge(START, "analyzer")
    graph.add_edge("analyzer", "classifier")
    graph.add_edge("classifier", "reasoner")
    graph.add_edge("reasoner", "ceo")
    graph.add_edge("ceo", "research")
    graph.add_edge("research", "engineer")
    graph.add_edge("engineer", "qa")
    graph.add_edge("qa", "approval")
    graph.add_edge("approval", "planner")
    graph.add_edge("planner", END)

    return graph.compile()