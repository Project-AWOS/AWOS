from typing import TypedDict
from app.models.analysis import MissionAnalysis
from app.models.classification import MissionClassification
from app.models.reasoning import MissionReasoning
from app.models.planning import MissionPlan


class MissionState(TypedDict):
    mission: str

    analysis: MissionAnalysis | None
    classification: MissionClassification | None
    reasoning: MissionReasoning | None
    plan: MissionPlan | None