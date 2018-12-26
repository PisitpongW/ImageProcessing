import cv2
from matplotlib import pyplot as plt
import numpy as np

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(2,2,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

sobelx = cv2.Sobel(lsy,cv2.CV_64F,1,0,ksize=5)
plt.subplot(2,2,2),plt.imshow(sobelx,cmap = 'gray')
plt.title('sobel x'), plt.xticks([]), plt.yticks([])

sobely = cv2.Sobel(lsy,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,3),plt.imshow(sobely,cmap = 'gray')
plt.title('sobel y'), plt.xticks([]), plt.yticks([])

sobel = sobelx + sobely
plt.subplot(2,2,4),plt.imshow(sobel,cmap = 'gray')
plt.title('sobel'), plt.xticks([]), plt.yticks([])

plt.show()