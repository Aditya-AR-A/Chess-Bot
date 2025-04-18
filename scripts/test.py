import cv2
import mss
import numpy as np
from ultralytics import YOLO

# Load your trained YOLOv11m model
model = YOLO("D:\\Data Science\\Chess Bot\\model_data\\yolo11m\\detect\\train\\weights\\best.pt")  # Update this path

with mss.mss() as sct:
    monitor = sct.monitors[1]  # Fullscreen monitor, or adjust with monitor dict
    while True:
        # Grab a screenshot
        sct_img = sct.grab(monitor)

        # Convert to NumPy and BGR for OpenCV
        img = np.array(sct_img)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

        # Run YOLO detection on this frame
        results = model(img)

        # Draw the detection boxes
        annotated_img = results[0].plot()

        # Show the result
        cv2.imshow("YOLOv11m Chess Detection", annotated_img)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()
