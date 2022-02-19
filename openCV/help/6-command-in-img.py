import numpy as np
import cv2 as cv

img = cv.imread('images.jfif',cv.IMREAD_COLOR)

part = img[100:200,100:200]

img[100:200,100:200] = [255,255,255]

cv.imshow('window',img)

cv.waitKey()

img[100:200,100:200] = part

cv.imshow('title',img)

cv.waitKey()

cv.destroyAllWindows()
