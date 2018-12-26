import cv2
import numpy as np
import matplotlib.pyplot as plt

filejpg = "D:\Work\Image_Processing\Blog\py_code\lee-sung-kyung.jpg"
imgjpg = cv2.imread(filejpg,0)

hist_jpg,bins=np.histogram(imgjpg.flatten(),256,[0,255])
cdf_jpg=hist_jpg.cumsum()
plt.plot(cdf_jpg,color='b'),plt.grid('off'),plt.title('JPG CDF'),plt.show()

eq_jpg=cv2.equalizeHist(imgjpg)
hist_eq_jpg,bins=np.histogram(eq_jpg.flatten(),256,[0,256])
cdf_eq_jpg=hist_eq_jpg.cumsum()
plt.plot(cdf_jpg,color='b'),plt.plot(cdf_eq_jpg,color='r')
plt.title('JPG CDF'),plt.legend(('Normal','Equalized'),loc='upper left'),plt.show()