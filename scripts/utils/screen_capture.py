import mss
import numpy as np
import cv2
import time

class ScreenCapture:
    def __init__(self, monitor_index=1, fps=5):
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor_index]
        self.fps = fps
        self.interval = 1 / fps
        self.last_capture_time = 0
        self.last_frame = None

    def get_frame(self):
        current_time = time.time()
        if current_time - self.last_capture_time >= self.interval:
            sct_img = self.sct.grab(self.monitor)
            frame = np.array(sct_img)
            self.last_frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
            self.last_capture_time = current_time
        return self.last_frame
