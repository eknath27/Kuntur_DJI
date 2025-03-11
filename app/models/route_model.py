from pydantic import BaseModel
from typing import List

class RouteModel(BaseModel):
    name: str
    waypoints: List[dict]  # Lista de {"lat": float, "lon": float}