import cv2
import numpy as np

img1 = cv2.imread('image_back.jpg')

img2 = cv2.imread('amogus.jpg')

rows,cols,channels = img2.shape

roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#Background Delete

ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask)

img2_bg = cv2.bitwise_and(img2,img2,mask=mask_inv)

dst = cv2.add(img1_bg,img2_bg)

img1[0:rows,0:cols] = dst

cv2.imshow('Image Gray',img2gray)
cv2.imshow('mask',mask)
cv2.imshow('mask invert',mask_inv)
cv2.imshow("img1_bg",img1_bg)
cv2.imshow("img2_bg",img2_bg)
cv2.imshow('Added',dst)
cv2.imshow('Return',img1)
cv2.waitKey(0)

cv2.destroyAllWindows()
