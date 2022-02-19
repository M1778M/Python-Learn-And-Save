import cv2
import numpy as np



cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    lapacian = cv2.Laplacian(frame,cv2.CV_8U)
    
    sobelx = cv2.Sobel(frame,cv2.CV_8U,1,0,ksize=5)
    
    sobely = cv2.Sobel(frame,cv2.CV_8U,0,1,ksize=5)
    
    canny = cv2.Canny(frame,100,200)
    
    cv2.imshow('lap',lapacian)
    cv2.imshow('frame',frame)
    cv2.imshow('sobelX',sobelx)
    cv2.imshow('sobelY',sobely)
    cv2.imshow('Canny',canny)
    
    if (cv2.waitKey(5) & 0xFF) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()