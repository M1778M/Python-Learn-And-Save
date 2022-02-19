import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('face_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 0.6, 2)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('frame',frame)

    if (cv2.waitKey(27) & 0xFF) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()