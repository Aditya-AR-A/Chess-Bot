import cv2
import mss
import numpy as np

with mss.mss() as sct:
    monitor = sct.monitors[1]
    while True:
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

        cv2.imshow('Screen Capture', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()