"""
To observe false contouring
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('ctskull.tif', 0)

# cv.imshow('img', img)
# cv.waitKey(0)

# cv.imshow('a', a)
# cv.waitKey(0)


images = []
titles = []

bits = [8, 6, 5, 4, 3, 2, 1]
for k in range(len(bits)):
    levels = 2 ** bits[k]
    divsion_size = 256 / levels

    new_img = np.array(img / divsion_size, dtype='uint8')

    a = np.array(new_img * divsion_size + divsion_size / 2, dtype='uint8')

    images.append(a)
    titles.append("levels = " + str(levels))

for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv.destroyAllWindows()
