import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Fig1005(a)(wirebond_mask).tif', 0)

h, w = img.shape

vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
horizontal = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

newhorizontalImage = np.zeros((h, w))
newverticalImage = np.zeros((h, w))
newgradientImage = np.zeros((h, w))

for i in range(1, h - 1):
    for j in range(1, w - 1):
        horizontalGrad = (horizontal[0, 0] * img[i - 1, j - 1]) + (horizontal[0, 1] * img[i - 1, j]) + (
                     horizontal[0, 2] * img[i - 1, j + 1]) + (horizontal[1, 0] * img[i, j - 1]) + (
                     horizontal[1, 1] * img[i, j]) + (horizontal[1, 2] * img[i, j + 1]) + (
                     horizontal[2, 0] * img[i + 1, j - 1]) + (horizontal[2, 1] * img[i + 1, j]) + (
                     horizontal[2, 2] * img[i + 1, j + 1])
        newhorizontalImage[i - 1, j - 1] = abs(horizontalGrad)

        verticalGrad = (vertical[0, 0] * img[i - 1, j - 1]) + (vertical[0, 1] * img[i - 1, j]) + (
                     vertical[0, 2] * img[i - 1, j + 1]) + (vertical[1, 0] * img[i, j - 1]) + (
                     vertical[1, 1] * img[i, j]) + (vertical[1, 2] * img[i, j + 1]) + (
                     vertical[2, 0] * img[i + 1, j - 1]) + (vertical[2, 1] * img[i + 1, j]) + (
                     vertical[2, 2] * img[i + 1, j + 1])
        newverticalImage[i - 1, j - 1] = abs(verticalGrad)

        mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
        newgradientImage[i - 1, j - 1] = mag

r = newgradientImage.astype(np.uint8)

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
