import cv2
import numpy as np
from matplotlib import pyplot as plt

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(1,2,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

lsy_inv = 255 - lsy
plt.subplot(1,2,2),plt.imshow(lsy_inv,cmap = 'gray')
plt.title('convert'), plt.xticks([]), plt.yticks([])

plt.show()