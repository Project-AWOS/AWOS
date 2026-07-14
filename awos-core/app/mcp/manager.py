"""
=========================================================
Module      : manager.py

System      : AWOS

Component   : MCP Manager

Purpose
-------
Provides a generic interface for communicating with
external MCP servers.

Agents should use this manager instead of interacting
with the MCP client directly.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from typing import Any

from app.mcp.client import mcp_client


class MCPManager:
    """
    High-level MCP manager.

    All agents communicate with external MCP servers
    through this manager.
    """

    async def call(
        self,
        server: str,
        tool: str,
        arguments: dict[str, Any],
    ):
        """
        Execute a tool on the specified MCP server.

        Parameters
        ----------
        server : str
            MCP server name (github, slack, filesystem...)

        tool : str
            Tool name exposed by the MCP server.

        arguments : dict
            Tool arguments.

        Returns
        -------
        Any
            Tool execution result.
        """

        return await mcp_client.call_tool(
            server=server,
            tool=tool,
            arguments=arguments,
        )


mcp_manager = MCPManager()
