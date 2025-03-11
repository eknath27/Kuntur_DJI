from fastapi import FastAPI
from app.routes import drone_routes, video_routes

app = FastAPI(title="DJI Tello Surveillance API")

app.include_router(drone_routes.router, prefix="/drone")
app.include_router(video_routes.router, prefix="/video")

@app.get("/")
def read_root():
    return {"message": "API para control de vigilancia con DJI Tello"}
