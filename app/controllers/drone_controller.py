from djitellopy import Tello
import cv2
import time
import threading

class DroneController:
    def __init__(self):
        self.tello = Tello()
        self.video_writer = None
        self.recording = False

    def connect(self):
        self.tello.connect()
        self.tello.streamon()

    def start_recording(self, filename="videos/output.avi"):
        frame_read = self.tello.get_frame_read()
        self.video_writer = cv2.VideoWriter(
            filename, cv2.VideoWriter_fourcc(*"XVID"), 30, (frame_read.frame.shape[1], frame_read.frame.shape[0])
        )
        self.recording = True

        def record():
            while self.recording:
                frame = frame_read.frame
                self.video_writer.write(frame)
                time.sleep(1 / 30)

        threading.Thread(target=record, daemon=True).start()

    def stop_recording(self):
        self.recording = False
        if self.video_writer:
            self.video_writer.release()

    def follow_route(self, route):
        self.tello.takeoff()
        self.start_recording()

        for point in route.points:
            print(f"Moviendo a latitud {point.latitude}, longitud {point.longitude}")
            self.tello.move_forward(20)  # Simulación del movimiento

        self.stop_recording()
        self.tello.land()

