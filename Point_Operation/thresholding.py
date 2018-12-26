import cv2
import numpy as np
from matplotlib import pyplot as plt

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(1,4,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

ret,thresh1 = cv2.threshold(lsy,63,255,cv2.THRESH_BINARY)
plt.subplot(1,4,2),plt.imshow(thresh1,cmap = 'gray')
plt.title('thresh at 63'), plt.xticks([]), plt.yticks([])

ret,thresh2 = cv2.threshold(lsy,127,255,cv2.THRESH_BINARY)
plt.subplot(1,4,3),plt.imshow(thresh2,cmap = 'gray')
plt.title('thresh at 127'), plt.xticks([]), plt.yticks([])

ret,thresh3 = cv2.threshold(lsy,191,255,cv2.THRESH_BINARY)
plt.subplot(1,4,4),plt.imshow(thresh3,cmap = 'gray')
plt.title('thresh at 191'), plt.xticks([]), plt.yticks([])

plt.show()