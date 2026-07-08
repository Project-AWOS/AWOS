from app.mcp.registry import registry

print(registry.list_servers())

print(registry.get("github"))
