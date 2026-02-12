import cv2
import numpy as np

def detect_color(frame):

    frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hgt, wdt, _ = frame.shape
    cx, cy = wdt // 2, hgt // 2
    radius = 25

    mask = np.zeros((hgt, wdt), dtype=np.uint8)
    cv2.circle(mask, (cx, cy), radius, 255, -1)

    h = int(np.mean(hsv[:,:,0][mask==255]))
    s = int(np.mean(hsv[:,:,1][mask==255]))
    v = int(np.mean(hsv[:,:,2][mask==255]))

    color = "Undefined"

    if s < 40 and v > 200:
        color = "White"
    elif h < 10 or h >= 170:
        color = "Red"
    elif h < 25:
        color = "Orange"
    elif h < 35:
        color = "Yellow"
    elif h < 85:
        if v > 180:
            color = "Light Green"
        else:
            color = "Green"
    elif h < 130:
        if v > 180:
            color = "Sky Blue"
        else:
            color = "Blue"
    elif h < 160:
        color = "Violet"

    # Draw circle
    cv2.circle(frame, (cx, cy), radius, (255,0,0), 2)

    # Dynamic BGR text color
    b = int(np.mean(frame[:,:,0][mask==255]))
    g = int(np.mean(frame[:,:,1][mask==255]))
    r = int(np.mean(frame[:,:,2][mask==255]))
    text_color = (b, g, r)

    cv2.putText(frame, color, (30,60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, text_color, 3)

    return frame, color
