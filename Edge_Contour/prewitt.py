import cv2
from matplotlib import pyplot as plt
import numpy as np

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

plt.subplot(2,2,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

prewittx = cv2.filter2D(lsy, -1, kernelx)
plt.subplot(2,2,2),plt.imshow(prewittx,cmap = 'gray')
plt.title('prewitt x'), plt.xticks([]), plt.yticks([])

prewitty = cv2.filter2D(lsy, -1, kernely)
plt.subplot(2,2,3),plt.imshow(prewitty,cmap = 'gray')
plt.title('prewitt y'), plt.xticks([]), plt.yticks([])

prewitt = prewittx + prewitty
plt.subplot(2,2,4),plt.imshow(prewitt,cmap = 'gray')
plt.title('prewitt'), plt.xticks([]), plt.yticks([])

plt.show()