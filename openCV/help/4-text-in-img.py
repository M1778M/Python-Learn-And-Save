import cv2 as cv
import numpy as np

img = cv.imread('images.jfif',cv.IMREAD_ANYCOLOR)

cv.line(img,(100,200),(100,-200),(0,0,0),5)

cv.rectangle(img,(140,150),(100,200),(0,0,255),3)

cv.imshow('title',img)





cv.waitKey()
cv.destroyAllWindows()