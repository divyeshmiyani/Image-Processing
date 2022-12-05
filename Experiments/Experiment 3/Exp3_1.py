# 1

"""
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('2.jpg',1)
# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
print(sum(histr))
plt.show()
"""

import cv2
from matplotlib import pyplot as plt

# reading the input image
img = cv2.imread('2.jpg')

# define colors to plot the histograms
colors = ('b', 'g', 'r')

# compute and plot the image histograms
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Image Histogram GFG')
plt.show()
