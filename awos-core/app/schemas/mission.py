from pydantic import BaseModel
from typing import Optional


class MissionCreate(BaseModel):
    title: str
    objective: str
    priority: str = "Medium"


class MissionResponse(BaseModel):
    mission_id: str
    title: str
    objective: str
    priority: str
    status: str