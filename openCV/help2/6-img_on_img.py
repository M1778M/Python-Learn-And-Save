import cv2
import numpy as np

img = cv2.imread('img1.jpg')
img2 = cv2.imread('img1c.jpg')


add = img + img2
# or 
add2 = cv2.add(img,img2)

add3 = cv2.addWeighted(img,0.5,img2,0.7,0)

# cv2.imshow('s',img)
# cv2.imshow('',img2)

cv2.imshow('What',add)

cv2.imshow('What2',add2)

cv2.imshow('what3',add3)



cv2.waitKey(0)
cv2.destroyAllWindows()