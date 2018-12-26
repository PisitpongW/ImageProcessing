import cv2
from matplotlib import pyplot as plt
import numpy as np

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)
kernel = np.ones((3,3),np.uint8)

plt.subplot(1,3,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

opening = cv2.morphologyEx(lsy, cv2.MORPH_OPEN, kernel)
plt.subplot(1,3,2),plt.imshow(opening,cmap = 'gray')
plt.title('opening'), plt.xticks([]), plt.yticks([])

closing = cv2.morphologyEx(lsy, cv2.MORPH_CLOSE, kernel)
plt.subplot(1,3,3),plt.imshow(closing,cmap = 'gray')
plt.title('closing'), plt.xticks([]), plt.yticks([])

plt.show()
