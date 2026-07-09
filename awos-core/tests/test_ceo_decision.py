import anyio

from app.cortex.analyzer import analyze_mission
from app.cortex.classifier import classify_mission
from app.agents.ceo import CEOAgent


async def main():

    mission = input("Mission: ")

    analysis = analyze_mission(mission)

    classification = classify_mission(analysis)

    decision = CEOAgent().decide(
        analysis,
        classification,
    )

    print("\n===== CEO DECISION =====")
    print(decision.model_dump())


if __name__ == "__main__":
    anyio.run(main)
