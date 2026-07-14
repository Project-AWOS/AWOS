from app.cortex.analyzer import analyze_mission
from app.cortex.classifier import classify_mission
from app.cortex.reasoner import MissionReasoner
from app.cortex.planner import create_execution_plan


MISSION = """
Build a hospital appointment system using FastAPI.

The application should support
patient registration,
doctor schedules,
appointment booking,
Docker deployment.

"""


def main():

    print("\n========== ANALYZER ==========\n")

    analysis = analyze_mission(MISSION)

    print(analysis.model_dump_json(indent=4))

    print("\n========== CLASSIFIER ==========\n")

    classification = classify_mission(analysis)

    print(classification.model_dump_json(indent=4))

    print("\n========== REASONER ==========\n")

    reasoner = MissionReasoner()

    reasoning = reasoner.reason(
        analysis,
        classification,
    )

    print(reasoning.model_dump_json(indent=4))

    print("\n========== PLANNER ==========\n")

    plan = create_execution_plan(reasoning)

    print(plan.model_dump_json(indent=4))


if __name__ == "__main__":
    main()