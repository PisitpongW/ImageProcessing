import cv2
from matplotlib import pyplot as plt
import numpy as np

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(1,3,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

canny = cv2.Canny(lsy,100,200)
plt.subplot(1,3,2),plt.imshow(canny,cmap = 'gray')
plt.title('canny'), plt.xticks([]), plt.yticks([])

lsy = cv2.GaussianBlur(lsy,(5,5),0)
laplace = cv2.Laplacian(lsy,cv2.CV_64F)
plt.subplot(1,3,3),plt.imshow(laplace,cmap = 'gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])

plt.show()