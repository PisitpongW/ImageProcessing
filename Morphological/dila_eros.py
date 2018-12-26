import cv2
from matplotlib import pyplot as plt
import numpy as np

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)
kernel = np.ones((3,3),np.uint8)

plt.subplot(1,3,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

dilation = cv2.dilate(lsy,kernel,iterations = 1)
plt.subplot(1,3,2),plt.imshow(dilation,cmap = 'gray')
plt.title('dilation'), plt.xticks([]), plt.yticks([])

erosion = cv2.erode(lsy,kernel,iterations = 1)
plt.subplot(1,3,3),plt.imshow(erosion,cmap = 'gray')
plt.title('erosion'), plt.xticks([]), plt.yticks([])

plt.show()
