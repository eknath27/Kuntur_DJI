from fastapi import FastAPI
from app.routes import drone_routes

app = FastAPI()
app.include_router(drone_routes.router)

@app.get("/")
async def root():
    return {"message": "Sistema de vigilancia con DJI Tello"}
