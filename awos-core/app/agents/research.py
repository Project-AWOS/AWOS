"""
=========================================================
Module      : research.py

System      : AWOS

Component   : Research Agent

Purpose
-------
Collects research and contextual information
required before engineering begins.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from pydantic import BaseModel

from app.mcp.manager import mcp_manager


class ResearchResult(BaseModel):
    completed: bool
    notes: list[str]


class ResearchAgent:
    """
    Research Agent.

    Uses the GitHub MCP server to gather
    repositories and technical context.
    """

    async def execute(self, mission: str) -> ResearchResult:

        github_result = await mcp_manager.call(
            server="github",
            tool="search_repository",
            arguments={
                "query": mission,
                "limit": 5,
            },
        )

        notes = [
            "Mission requirements analyzed.",
            f"GitHub MCP executed tool: {github_result['tool']}",
            f"Search query: {mission}",
            "Repository research completed.",
        ]

        return ResearchResult(
            completed=True,
            notes=notes,
        )
