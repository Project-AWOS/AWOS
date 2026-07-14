import anyio

from app.agents.research import ResearchAgent


async def main():

    mission = input("Enter mission: ")

    result = await ResearchAgent().execute(mission)

    print("\n===== RESEARCH RESULT =====")
    print(result.model_dump())


if __name__ == "__main__":
    anyio.run(main)
