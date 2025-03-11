from djitellopy import Tello
import time

class DroneController:
    def __init__(self):
        self.tello = Tello()
        self.tello.connect()

    def takeoff(self):
        self.tello.takeoff()
        return {"message": "Dron despegó"}

    def land(self):
        self.tello.land()
        return {"message": "Dron aterrizó"}

    def execute_route(self, route):
        self.takeoff()
        for _ in route:  # Simulación de ruta
            self.tello.move_forward(50)
            time.sleep(2)
        self.land()
        return {"message": "Ruta completada"}

    def start_video(self):
        self.tello.streamon()
        return self.tello.get_frame_read().frame

    def stop_video(self):
        self.tello.streamoff()
        return {"message": "Grabación detenida"}
