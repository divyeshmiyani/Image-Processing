"""
To observe checkerboard effect
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Rose.tif', 0)

# cv.imshow('img', img)
# cv.waitKey(0)
images = []
s = [1, 2, 6, 10, 16, 20]
for k in range(len(s)):
    new_img = []
    for i in range(0, img.shape[0], s[k]):
        row = []
        for j in range(0, img.shape[1], s[k]):
            row.append(img[i][j])
        new_img.append(row)

    new_img = np.array(new_img, dtype='uint8')

    # cv.imshow('new_img', new_img)
    # cv.waitKey(0)

    images.append(new_img)

titles = ['original', 'drop of 1', 'drop of 5', 'drop of 9', 'drop of 15', 'drop of 19']
for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv.destroyAllWindows()
