import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('samsung_logo.png',0)
logo = cv2.imread('samsung_logo_cuted.png',0)


orb = cv2.ORB_create()

kp1,des1 = orb.detectAndCompute(logo,None)
kp2,des2 = orb.detectAndCompute(img,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda x:x.distance)

img_out = cv2.drawMatches(img,kp2,logo,kp1,matches,None,flags=2)

cv2.imshow('img',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
