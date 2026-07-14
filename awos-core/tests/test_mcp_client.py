from app.mcp.client import mcp_client

result = mcp_client.call_tool(
    server="github",
    tool="search_repository",
    arguments={
        "query": "FastAPI authentication"
    }
)

print(result)
