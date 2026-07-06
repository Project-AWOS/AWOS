"""
=========================================================
Module      : planning.py

System      : AWOS

Component   : Models

Purpose
-------
Defines the execution plan generated
by the Planner.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    """
    Represents one execution step.
    """

    order: int
    agent: str
    action: str


class MissionPlan(BaseModel):
    """
    Structured execution plan.
    """

    summary: str

    steps: list[PlanStep] = Field(default_factory=list)

    tools: list[str] = Field(default_factory=list)