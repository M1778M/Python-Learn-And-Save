import cv2 as cv
import numpy as np

img = cv.imread('images.jfif',cv.IMREAD_ANYCOLOR)

cv.circle(img,(100,100),70,(0,255,0),6)

pts = np.array([[133,145],[113,156],[173,167],[186,112],[145,163],[166,122]])

cv.polylines(img,[pts],True,(120,0,50),3) # True or False

font = cv.FONT_HERSHEY_COMPLEX

cv.putText(img,'hello',(100,100),font,1,(0,0,0),4)

cv.imshow('title',img)


cv.waitKey()
cv.destroyAllWindows()