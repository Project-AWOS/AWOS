"""
=========================================================
Module      : planner.py

System      : AWOS

Component   : CORTEX

Purpose
-------
Creates an execution plan from the
AI-generated mission reasoning.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from app.models.reasoning import MissionReasoning
from app.models.planning import MissionPlan, PlanStep


def create_execution_plan(
    reasoning: MissionReasoning,
) -> MissionPlan:
    """
    Convert MissionReasoning into
    a structured MissionPlan.
    """

    steps = []

    for index, action in enumerate(reasoning.execution_strategy, start=1):

        # Assign an agent in order
        if index <= len(reasoning.required_agents):
            agent = reasoning.required_agents[index - 1]
        else:
            agent = "Engineer"

        steps.append(
            PlanStep(
                order=index,
                agent=agent,
                action=action,
            )
        )

    return MissionPlan(
        summary=reasoning.summary,
        steps=steps,
        tools=reasoning.required_tools,
    )
