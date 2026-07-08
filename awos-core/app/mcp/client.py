"""
=========================================================
Module      : client.py

System      : AWOS

Component   : MCP Client

Purpose
-------
Thin wrapper around the official MCP SDK.

Author
------
Project AWOS Team

Version
-------
Genesis v1.0
=========================================================
"""

from typing import Any

import mcp.types as types

from mcp.client.session import ClientSession
from mcp.client.stdio import (
    StdioServerParameters,
    stdio_client,
)

from mcp.shared.message import SessionMessage
from mcp.shared.session import RequestResponder

from anyio.streams.memory import (
    MemoryObjectReceiveStream,
    MemoryObjectSendStream,
)

from app.mcp.registry import registry
import json


async def message_handler(
    message: RequestResponder[
        types.ServerRequest,
        types.ClientResult,
    ]
    | types.ServerNotification
    | Exception,
):
    """
    Handle server notifications.

    For now we simply ignore them.
    """

    if isinstance(message, Exception):
        print(message)


class MCPClient:

    async def call_tool(
        self,
        server: str,
        tool: str,
        arguments: dict[str, Any],
    ):

        config = registry.get(server)

        params = StdioServerParameters(
            command=config["command"],
            args=config["args"],
            env=config["env"],
        )

        async with stdio_client(params) as streams:

            return await self._execute(
                streams[0],
                streams[1],
                tool,
                arguments,
            )

    async def _execute(
        self,
        read_stream: MemoryObjectReceiveStream[
            SessionMessage | Exception
        ],
        write_stream: MemoryObjectSendStream[
            SessionMessage
        ],
        tool: str,
        arguments: dict[str, Any],
    ):

        async with ClientSession(
            read_stream,
            write_stream,
            message_handler=message_handler,
        ) as session:

            print("Initializing MCP Session...")

            await session.initialize()

            print("MCP Session Initialized")

            result = await session.call_tool(
                tool,
                arguments,
            )

            if result.isError:
                raise RuntimeError(result.content)

            if result.structuredContent is not None:
                return result.structuredContent

            if result.content:

                text = result.content[0].text

            try:
                return json.loads(text)

            except Exception:
                return {
                    "text": text
                }

            return {}


mcp_client = MCPClient()
