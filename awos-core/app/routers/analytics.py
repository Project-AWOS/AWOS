from fastapi import APIRouter

from app.services.mission_service import get_all_missions

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/")
def get_analytics():

    missions = get_all_missions()

    total = len(missions)

    created = sum(
        1 for mission in missions
        if mission["status"] == "Created"
    )

    running = sum(
        1 for mission in missions
        if mission["status"] == "Running"
    )

    completed = sum(
        1 for mission in missions
        if mission["status"] == "Completed"
    )

    failed = sum(
        1 for mission in missions
        if mission["status"] == "Failed"
    )

    success_rate = 0

    if total > 0:
        success_rate = round(
            (completed / total) * 100,
            2
        )

    return {
        "total_missions": total,
        "created": created,
        "running": running,
        "completed": completed,
        "failed": failed,
        "success_rate": success_rate,
    }   