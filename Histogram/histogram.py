import cv2
import numpy as np
import matplotlib.pyplot as plt
import imageio

# image getting
filebmp = 'D:\Work\Image_Processing\Converted\IMG_0633.bmp'
filegif = 'D:\Work\Image_Processing\Converted\IMG_0633.gif'
filetiff = 'D:\Work\Image_Processing\Converted\IMG_0633.tiff'
filepng = 'D:\Work\Image_Processing\Converted\IMG_0633.png'
filejpg = 'D:\Work\Image_Processing\Converted\IMG_0633.jpg'

imgbmp = cv2.imread(filebmp,0)
con = imageio.mimread(filegif)
imggif = cv2.cvtColor(con[0],cv2.COLOR_BGR2GRAY)
imgtiff = cv2.imread(filetiff,0)
imgpng = cv2.imread(filepng,0)
imgjpg = cv2.imread(filejpg,0)

# image showing
cv2.imshow('JPG image',imgjpg)
cv2.imshow('PNG image',imgpng)
cv2.imshow('GIF image',imggif)
cv2.imshow('TIFF image',imgtiff)
cv2.imshow('BMP image',imgbmp)
cv2.waitKey(0)
cv2.destroyAllWindows()



# histogram
hist_jpg,bins=np.histogram(imgjpg.flatten(),256,[0,255])
hist_png,bins=np.histogram(imgpng.flatten(),256,[0,255])
hist_gif,bins=np.histogram(imggif.flatten(),256,[0,255])
hist_tiff,bins=np.histogram(imgtiff.flatten(),256,[0,255])
hist_bmp,bins=np.histogram(imgbmp.flatten(),256,[0,255])

plt.plot(hist_jpg,color='b'),plt.title('JPG image histogram'),plt.show()
plt.plot(hist_png,color='b'),plt.title('PNG image histogram'),plt.show()
plt.plot(hist_gif,color='b'),plt.title('GIF image histogram'),plt.show()
plt.plot(hist_tiff,color='b'),plt.title('TIFF image histogram'),plt.show()
plt.plot(hist_bmp,color='b'),plt.title('BMP image histogram'),plt.show()



# cumulative histogram
cdf_jpg=hist_jpg.cumsum()
plt.plot(cdf_jpg,color='b'),plt.title('JPG CDF'),plt.show()
cdf_png=hist_png.cumsum()
plt.plot(cdf_png,color='b'),plt.title('PNG CDF'),plt.show()
cdf_gif=hist_gif.cumsum()
plt.plot(cdf_gif,color='b'),plt.title('GIF CDF'),plt.show()
cdf_tiff=hist_tiff.cumsum()
plt.plot(cdf_tiff,color='b'),plt.title('TIFF CDF'),plt.show()
cdf_bmp=hist_bmp.cumsum()
plt.plot(cdf_bmp,color='b'),plt.title('BMP CDF'),plt.show()



# image equalization
eq_jpg=cv2.equalizeHist(imgjpg)
eq_png=cv2.equalizeHist(imgpng)
eq_gif=cv2.equalizeHist(imggif)
eq_tiff=cv2.equalizeHist(imgtiff)
eq_bmp=cv2.equalizeHist(imgbmp)

cv2.imshow('Equalized JPG image',eq_jpg)
cv2.imshow('Equalized PNG image',eq_png)
cv2.imshow('Equalized GIF image',eq_gif)
cv2.imshow('Equalized TIFF image',eq_tiff)
cv2.imshow('Equalized BMP image',eq_bmp)
cv2.waitKey(0)
cv2.destroyAllWindows()



# cdf comparison
hist_eq_jpg,bins=np.histogram(eq_jpg.flatten(),256,[0,256])
cdf_eq_jpg=hist_eq_jpg.cumsum()
plt.plot(cdf_jpg,color='b'),plt.plot(cdf_eq_jpg,color='r')
plt.title('JPG CDF'),plt.legend(('Normal','Equalized'),loc='upper left'),plt.show()

hist_eq_png,bins=np.histogram(eq_png.flatten(),256,[0,256])
cdf_eq_png=hist_eq_png.cumsum()
plt.plot(cdf_png,color='b'),plt.plot(cdf_eq_png,color='r')
plt.title('PNG CDF'),plt.legend(('Normal','Equalized'),loc='upper left'),plt.show()

hist_eq_gif,bins=np.histogram(eq_gif.flatten(),256,[0,256])
cdf_eq_gif=hist_eq_gif.cumsum()
plt.plot(cdf_gif,color='b'),plt.plot(cdf_eq_gif,color='r')
plt.title('GIF CDF'),plt.legend(('Normal','Equalized'),loc='upper left'),plt.show()

hist_eq_tiff,bins=np.histogram(eq_tiff.flatten(),256,[0,256])
cdf_eq_tiff=hist_eq_tiff.cumsum()
plt.plot(cdf_tiff,color='b'),plt.plot(cdf_eq_tiff,color='r')
plt.title('TIFF CDF'),plt.legend(('Normal','Equalized'),loc='upper left'),plt.show()

hist_eq_bmp,bins=np.histogram(eq_bmp.flatten(),256,[0,256])
cdf_eq_bmp=hist_eq_bmp.cumsum()
plt.plot(cdf_bmp,color='b'),plt.plot(cdf_eq_bmp,color='r')
plt.title('BMP CDF'),plt.legend(('Normal','Equalized'),loc='upper left'),plt.show()