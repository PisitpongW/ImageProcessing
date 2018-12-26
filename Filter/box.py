import cv2
import numpy as np
from matplotlib import pyplot as plt

lsy = cv2.imread("D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg",0)

plt.subplot(1,4,1),plt.imshow(lsy,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

kernel3 = np.ones((3,3),np.float32)/9.0
blur3 = cv2.filter2D(lsy,-1,kernel3)
plt.subplot(1,4,2),plt.imshow(blur3,cmap = 'gray')
plt.title('3x3'), plt.xticks([]), plt.yticks([])

kernel5 = np.ones((5,5),np.float32)/25.0
blur5 = cv2.filter2D(lsy,-1,kernel5)
plt.subplot(1,4,3),plt.imshow(blur5,cmap = 'gray')
plt.title('5x5'), plt.xticks([]), plt.yticks([])

kernel7 = np.ones((7,7),np.float32)/49.0
blur7 = cv2.filter2D(lsy,-1,kernel7)
plt.subplot(1,4,4),plt.imshow(blur7,cmap = 'gray')
plt.title('7x7'), plt.xticks([]), plt.yticks([])

plt.show()