import anyio

from app.mcp.manager import mcp_manager


async def main():

    result = await mcp_manager.github(
        "search_repository",
        {
            "query": "FastAPI",
            "limit": 3,
        },
    )

    print(result)


if __name__ == "__main__":
    anyio.run(main)
