import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier("face.xml")
eyes_detector = cv2.CascadeClassifier("eyes.xml")

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_detector.detectMultiScale(gray)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eyes_detector.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
    
    cv2.imshow('Face.exe',frame)
    
    if (cv2.waitKey(27) & 0xFF) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()