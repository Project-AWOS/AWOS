from pprint import pprint

from github_mcp.intelligence import research_repository


result = research_repository(
    "fastapi authentication"
)

print("\n========== AWOS GitHub Intelligence ==========\n")

pprint(result)

print("\n==============================================")
