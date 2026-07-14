import anyio

from app.mcp.client import mcp_client


async def main():

    result = await mcp_client.call_tool(
        server="github",
        tool="create_repository_branch",
        arguments={
            "owner": "manaswitha7",
            "repo_name": "awos-engineer-demo",
            "branch_name": "feature/awos",
            "source_branch": "main",
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
