import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fg = cv2.createBackgroundSubtractorMOG2()

while True:
    _,frame = cap.read()
    
    fmask = fg.apply(frame)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',fmask)
    
    
    if (cv2.waitKey(27) & 0xFF) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()