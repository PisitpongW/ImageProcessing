import cv2
import numpy as np
from matplotlib import pyplot as plt

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(1,4,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

median3 = cv2.medianBlur(lsy,3)
plt.subplot(1,4,2),plt.imshow(median3,cmap = 'gray')
plt.title('median 3'), plt.xticks([]), plt.yticks([])

median5 = cv2.medianBlur(lsy,5)
plt.subplot(1,4,3),plt.imshow(median5,cmap = 'gray')
plt.title('median 5'), plt.xticks([]), plt.yticks([])

median7 = cv2.medianBlur(lsy,7)
plt.subplot(1,4,4),plt.imshow(median7,cmap = 'gray')
plt.title('median 7'), plt.xticks([]), plt.yticks([])

plt.show()