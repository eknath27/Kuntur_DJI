from fastapi import APIRouter
from app.models.route_model import Route
from app.controllers.drone_controller import DroneController

router = APIRouter()
drone_controller = DroneController()

@router.post("/start_mission/")
async def start_mission(route: Route):
    drone_controller.connect()
    drone_controller.follow_route(route)
    return {"message": "Misión completada. Video guardado."}