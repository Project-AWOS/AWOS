import requests

from config import FASTAPI_URL


TIMEOUT = 30


def create_mission(title, objective=None, priority="Medium"):

    if objective is None:
        objective = title

    payload = {
        "title": title,
        "objective": objective,
        "priority": priority,
    }

    response = requests.post(
        f"{FASTAPI_URL}/missions/",
        json=payload,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def get_missions():

    response = requests.get(
        f"{FASTAPI_URL}/missions/",
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def get_mission(mission_id):

    response = requests.get(
        f"{FASTAPI_URL}/missions/{mission_id}",
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def delete_mission(mission_id):

    response = requests.delete(
        f"{FASTAPI_URL}/missions/{mission_id}",
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def execute_mission(mission_id):

    response = requests.post(
        f"{FASTAPI_URL}/missions/{mission_id}/execute",
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()

def get_analytics():

    response = requests.get(
        f"{FASTAPI_URL}/analytics/",
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()