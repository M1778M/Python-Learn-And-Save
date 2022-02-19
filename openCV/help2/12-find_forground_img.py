import cv2
import numpy as np

img = cv2.imread('shatranj.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,200,0.1,10)

corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),1)


cv2.imshow('Corners_',img)



cv2.waitKey(0)
cv2.destroyAllWindows()