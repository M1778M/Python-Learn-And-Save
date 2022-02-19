import cv2
import numpy as np
import keyboard as kb

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,10,0])
    upper_red = np.array([255,255,230])
    
    mask = cv2.inRange(hsv,lower_red,upper_red)
    
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    res2 = cv2.bitwise_not(mask)
    
    cv2.imshow('frame',frame)
    
    cv2.imshow('mask',mask)
    
    cv2.imshow('res',res)
    cv2.imshow('res2',res2)
    
    if (cv2.waitKey(5) & 0xFF) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()