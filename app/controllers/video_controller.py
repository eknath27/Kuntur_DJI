import cv2
import os
import time
from app.config import Config

class VideoController:
    def __init__(self):
        os.makedirs(Config.VIDEO_STORAGE_PATH, exist_ok=True)

    def record_video(self, drone):
        cap = cv2.VideoCapture(0)
        filename = f"{Config.VIDEO_STORAGE_PATH}video_{int(time.time())}.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

        start_time = time.time()
        while time.time() - start_time < 10:  # Grabar por 10 segundos
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        return {"message": "Video grabado", "filename": filename}
