import cv2
from PIL import Image
from util import get_limits # This gets input from util.py

yellow = [0, 255, 255] 
cap = cv2.VideoCapture(0) 

lowerLimit, upperLimit = get_limits(color=yellow)

while True:
    ret, frame = cap.read()
    if not ret: break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    
    # Cleaning the mask to fix framing
    mask = cv2.medianBlur(mask, 7)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
