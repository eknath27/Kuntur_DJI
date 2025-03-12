from pydantic import BaseModel
from typing import List

class GPSPoint(BaseModel):
    latitude: float
    longitude: float

class Route(BaseModel):
    points: List[GPSPoint]

