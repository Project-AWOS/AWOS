"""
MCP Server Configuration
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

MCP_CONFIG = {
    "github": {
        "name": "GitHub MCP",
        "transport": "stdio",
        "command": "python",
        "args": [
            str(PROJECT_ROOT / "mcp-server" / "server.py")
        ],
        "env": {}
    }
}
