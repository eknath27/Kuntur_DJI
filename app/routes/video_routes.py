from fastapi import APIRouter
from app.controllers.video_controller import VideoController
from app.controllers.drone_controller import DroneController

router = APIRouter()
video_controller = VideoController()
drone = DroneController()

@router.post("/record")
def record_video():
    return video_controller.record_video(drone)
