from typing import Any


class MCPClient:
    """
    Thin wrapper around MCP communication.

    This class is the ONLY place that talks
    to external MCP servers.
    """

    async def call_tool(
        self,
        server: str,
        tool: str,
        arguments: dict[str, Any],
    ):

        print("=" * 60)
        print("MCP REQUEST")
        print("=" * 60)
        print("Server :", server)
        print("Tool   :", tool)
        print("Args   :", arguments)
        print("=" * 60)

        #
        # NEXT STEP
        #
        # Replace this section with the
        # official MCP SDK transport.
        #

        return {
            "status": "success",
            "server": server,
            "tool": tool,
            "arguments": arguments,
        }


mcp_client = MCPClient()
