import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('images.jfif',cv.IMREAD_GRAYSCALE)


plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([100,200],[100,200],'r',linewidth=5)
plt.show()

cv.imwrite('output.jfif',img)