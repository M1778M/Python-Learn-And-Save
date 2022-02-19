import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # cv2.line(frame,(100,200),(200,400),(255,0,0),10) # 10 = width of line / color = BGR
    # cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)
    
    cv2.circle(frame,(400,300),100,(0,255,0),3)
    
    pts = np.array([[300,200],[200,400],[600,200],[400,100]])
    
    cv2.polylines(frame,[pts],True,(200,70,80),2)
    
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'M1778',(100,100),font,3,(100,100,100),5)
    
    cv2.imshow('frame.exe',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()