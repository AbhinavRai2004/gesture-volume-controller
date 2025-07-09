import cv2 as cv
import mediapipe as mp
import numpy as np
import time 
import math
import hand_tracking_module as htm  # Make sure this file is present and correct

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################
wCam, hCam = 640, 480
################################

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = htm.handDetector(detectionCon=0.7)

# Audio device setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()  # Typically (-65.25, 0.0)
minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # Get thumb tip and index finger tip
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw points and line
        cv.circle(img, (x1, y1), 10, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 10, (255, 0, 255), cv.FILLED)
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        # Convert length to volume range
        vol = np.interp(length, [30, 180], [minVol, maxVol])
        volBar = np.interp(length, [30, 180], [400, 150])
        volPer = np.interp(length, [30, 180], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)

        # Optional visual feedback for very low/high
        if length < 30:
            cv.circle(img, (cx, cy), 15, (0, 255, 0), cv.FILLED)
        elif length > 180:
            cv.circle(img, (cx, cy), 15, (0, 0, 255), cv.FILLED)

    # Volume bar
    cv.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 2)
    cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)
    cv.putText(img, f'{int(volPer)} %', (40, 430), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (500, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
