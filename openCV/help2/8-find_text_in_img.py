import cv2
import numpy as np


img = cv2.imread('img_text.jpg')

#delete background

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,ths = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

ret2,gray_ths = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
# -> adaptive -> so cool
th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('img',img)

cv2.imshow('ths',ths)

cv2.imshow('gray',gray)

cv2.imshow('gray_ths',gray_ths)

cv2.imshow('th',th)


cv2.waitKey(0)
cv2.destroyAllWindows()