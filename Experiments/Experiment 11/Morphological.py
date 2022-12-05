import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the input image
imgpath = 'Fig1005(a)(wirebond_mask).tif'
img = cv2.imread(imgpath, 0)  # ‘0’ is for gray scale image
# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 1), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=3)

# cv2.imshow('Input', img)
# cv2.imshow('Eroded Output', img_erosion)
# Writing the output image
outpath = 'erosionOut.tif'
cv2.imwrite(outpath, img_erosion)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='binary')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 2, 2)
plt.imshow(img_erosion, cmap='binary')
plt.title('Eroded Image')
plt.xticks([])
plt.yticks([])
plt.show()
