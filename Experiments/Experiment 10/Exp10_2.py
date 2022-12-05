import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Fig1005(a)(wirebond_mask).tif', 0)

h, w = img.shape

vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

horizontal = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

r = cv2.filter2D(img, -1, horizontal)
# r = cv2.filter2D(img, -1, vertical)


titles = ['Original Image', 'result of using Sobel operator ']
images = [img, r]

no = 2
for k in range(no):
    plt.subplot(1, no, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()
