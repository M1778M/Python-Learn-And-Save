import cv2
import numpy

img = cv2.imread("img1.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow('COMPILER.exe',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
