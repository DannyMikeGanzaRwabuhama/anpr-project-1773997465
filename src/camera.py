import cv2

import sys
source = sys.argv[1] if len(sys.argv) > 1 else 0
try:
    source = int(source)
except ValueError:
    pass
cap = cv2.VideoCapture(source)
if not cap.isOpened():
    raise RuntimeError('Cannot open webcam')

while True:
    ok, frame = cap.read()
    if not ok:
        break

    cv2.imshow('Camera Test', frame)
    if (cv2.waitKey(1) & 0xFF) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
