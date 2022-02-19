import cv2
import numpy as np

img = cv2.imread('super_mario_findcoin.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

coin = cv2.imread('super_mario_coin.jpg',0)

w,h = coin.shape[::-1]

res = cv2.matchTemplate(img_gray,coin,cv2.TM_CCOEFF_NORMED)
ths = 0.6

loc = np.where(res >= ths)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0))

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()