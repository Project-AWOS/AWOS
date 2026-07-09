"""
=========================================================
Module      : approval.py

System      : AWOS

Component   : Approval Agent

Purpose
-------
Handles human approval before executing
critical actions.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from pydantic import BaseModel


class ApprovalResult(BaseModel):
    approved: bool
    message: str


class ApprovalAgent:
    """
    Human Approval Agent.

    Currently mocked.

    Later this will communicate with the
    Slack application.
    """

    def request(self) -> ApprovalResult:

        return ApprovalResult(
            approved=True,
            message="Mission approved.",
        )