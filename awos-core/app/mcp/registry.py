from app.mcp.config import MCP_CONFIG


class MCPRegistry:

    def __init__(self):
        self._servers = MCP_CONFIG

    def get(self, name: str):

        if name not in self._servers:
            raise ValueError(f"MCP Server '{name}' not found.")

        return self._servers[name]

    def list_servers(self):

        return list(self._servers.keys())


registry = MCPRegistry()
