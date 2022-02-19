#!
import cv2 as cv
import numpy as np

img = cv.imread('images.jfif',cv.IMREAD_GRAYSCALE)

cv.imshow('title',img)

cv.waitKey()
cv.destroyAllWindows()