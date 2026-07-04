from uuid import uuid4
from app.storage.memory_store import missions


def create_mission(title: str, objective: str, priority: str):
    """
    Create a new mission and store it temporarily.
    """

    mission_id = f"AW-{str(uuid4())[:8].upper()}"

    mission = {
        "mission_id": mission_id,
        "title": title,
        "objective": objective,
        "priority": priority,
        "status": "Created"
    }

    missions[mission_id] = mission

    return mission


def get_all_missions():
    """Return all missions."""
    return list(missions.values())


def get_mission(mission_id: str):
    """Return one mission."""
    return missions.get(mission_id)


def delete_mission(mission_id: str):
    """Delete a mission."""
    return missions.pop(mission_id, None)