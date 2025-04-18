from ultralytics import YOLO
import numpy as np

class BoardDetector:
    def __init__(self, model_path="model_data\\yolo11m\\detect\\train\\weights\\best.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame: np.ndarray):
        results = self.model.predict(frame, verbose=False, conf = 0.8)[0]
        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            detections.append({"bbox": (x1, y1, x2, y2), "class": cls_id, "conf": conf})
        return detections
