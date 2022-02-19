import cv2 as cv
import numpy as np

# WebCam
cam = cv.VideoCapture(0)
fours = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter('output.avi',fours,24.0,(640,480))
while True:
    ret,fream = cam.read()# BGR2GRAY / BGR2{}

    out.write(fream)

    cv.imshow('fream',fream)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
out.release()
cv.destroyAllWindows()
