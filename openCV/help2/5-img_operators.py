import cv2 
import numpy as np

img = cv2.imread('img2.jpg',cv2.IMREAD_COLOR)

px = img[100:200,100:200] = [255,255,255]

px2 = img[300:400,300:400]

img[100:200,100:200] = px2

img[200:300,200:300] = px


cv2.imshow('Hello World.exe',img)

cv2.waitKey(0)
cv2.destroyAllWindows()