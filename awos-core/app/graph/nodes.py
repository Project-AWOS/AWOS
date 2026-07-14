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
from app.agents.ceo import CEOAgent
from app.agents.research import ResearchAgent
from app.agents.engineer import EngineerAgent
from app.agents.qa import QAAgent
from app.agents.approval import ApprovalAgent

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


async def research_node(state: MissionState) -> MissionState:
    """
    Execute Research Agent only if approved by CEO.
    """

    if not state["decision"].use_research:
        print("CEO -> Research Agent : SKIPPED")
        return state

    print("CEO -> Research Agent : EXECUTE")

    state["research"] = await ResearchAgent().execute(
        state["mission"]
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


def ceo_node(state: MissionState) -> MissionState:
    """
    Execute CEO decision.
    """

    state["decision"] = CEOAgent().decide(
        state["analysis"],
        state["classification"],
    )

    return state


async def engineer_node(state: MissionState) -> MissionState:
    """
    Execute Engineer Agent only if approved by CEO.
    """

    if not state["decision"].use_engineer:
        print("CEO -> Engineer Agent : SKIPPED")
        return state

    print("CEO -> Engineer Agent : EXECUTE")

    state["engineering"] = await EngineerAgent().execute(
        repo_name="awos-langgraph-demo",
        description=state["mission"],
        owner="manaswitha7",
    )

    return state


async def qa_node(state: MissionState) -> MissionState:
    """
    Execute QA Agent only if approved by CEO.
    """

    if not state["decision"].use_qa:
        print("CEO -> QA Agent : SKIPPED")
        return state

    print("CEO -> QA Agent : EXECUTE")

    state["qa"] = await QAAgent().execute()

    return state


def approval_node(state: MissionState) -> MissionState:
    """
    Execute Approval Agent.
    """

    state["approval"] = ApprovalAgent().request()

    return state
