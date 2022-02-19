import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread("img1.jpg",cv2.IMREAD_GRAYSCALE)

# cv2.imshow('COMPILER.exe',img)

plt.imshow(img,cmap="gray",interpolation='bicubic')
plt.plot([100,200],[150,200],'r',linewidth=10)
plt.show()


cv2.imwrite('save_img1.jpg',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

