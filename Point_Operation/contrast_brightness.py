import cv2
import numpy as np
from matplotlib import pyplot as plt

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(1,4,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

lsy2 = cv2.addWeighted(lsy, 0.5, np.zeros(lsy.shape, lsy.dtype), 0, 30)
plt.subplot(1,4,2),plt.imshow(lsy2,cmap = 'gray')
plt.title('I x 0.5 + 30'), plt.xticks([]), plt.yticks([])

lsy3 = cv2.addWeighted(lsy, 1.1, np.zeros(lsy.shape, lsy.dtype), 0, 10)
plt.subplot(1,4,3),plt.imshow(lsy3,cmap = 'gray')
plt.title('I x 1.1 + 10'), plt.xticks([]), plt.yticks([])

lsy4 = cv2.addWeighted(lsy, 1.5, np.zeros(lsy.shape, lsy.dtype), 0, -20)
plt.subplot(1,4,4),plt.imshow(lsy4,cmap = 'gray')
plt.title('I x 1.5 - 20'), plt.xticks([]), plt.yticks([])

plt.show()