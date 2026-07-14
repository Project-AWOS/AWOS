import anyio

from app.mcp.client import mcp_client


async def main():

    result = await mcp_client.call_tool(
        server="github",
        tool="update_repository_file",
        arguments={
            "owner": "manaswitha7",
            "repo_name": "awos-engineer-demo",
            "file_path": "README.md",
            "new_content": """# AWOS Engineer Demo

Created through AWOS MCP Integration.

## Features

- GitHub MCP
- LangGraph
- AI Agents
- Research Agent
- Engineer Agent
- QA Agent
""",
            "commit_message": "Update README",
            "branch": "feature/awos",
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
