from fastapi import APIRouter, HTTPException

from app.schemas.mission import MissionCreate
from app.services.mission_service import (
    create_mission,
    get_all_missions,
    get_mission,
    delete_mission,
)
from app.services.execution_service import execute_mission

router = APIRouter(
    prefix="/missions",
    tags=["Missions"]
)


@router.post("/")
def create(data: MissionCreate):
    return create_mission(
        title=data.title,
        objective=data.objective,
        priority=data.priority
    )


@router.get("/")
def get_all():
    return get_all_missions()


@router.get("/{mission_id}")
def get_one(mission_id: str):
    mission = get_mission(mission_id)

    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")

    return mission


@router.delete("/{mission_id}")
def delete(mission_id: str):
    mission = delete_mission(mission_id)

    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")

    return {
        "message": "Mission deleted successfully"
    }


@router.post("/{mission_id}/execute")
async def execute(mission_id: str):

    mission = get_mission(mission_id)

    if mission is None:
        raise HTTPException(
            status_code=404,
            detail="Mission not found",
        )

    plan = await execute_mission(
        mission["objective"]
    )

    return {
        "mission": mission,
        "execution_plan": plan,
    }
