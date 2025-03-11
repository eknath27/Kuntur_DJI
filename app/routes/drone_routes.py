from fastapi import APIRouter
from app.controllers.drone_controller import DroneController
from app.models.route_model import RouteModel

router = APIRouter()
drone = DroneController()

@router.post("/takeoff")
def takeoff():
    return drone.takeoff()

@router.post("/land")
def land():
    return drone.land()

@router.post("/route")
def execute_route(route: RouteModel):
    return drone.execute_route(route.waypoints)

@router.post("/start_video")
def start_video():
    return drone.start_video()

@router.post("/stop_video")
def stop_video():
    return drone.stop_video()