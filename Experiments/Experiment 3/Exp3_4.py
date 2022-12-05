import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('low-contrast-image.png', 0)
final = np.zeros((img.shape[0], img.shape[1]), dtype='float16')

histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

r1 = 70
r2 = 150
s1 = 0
s2 = 255

m1 = s1 / r1
m2 = (s2 - s1) / (r2 - r1)
m3 = (256 - s2) / (256 - r2)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] <= r1:
            final[i, j] = m1 * img[i][j]
        elif img[i][j] <= r2:
            final[i, j] = m2 * img[i][j]
        else:
            final[i, j] = m3 * img[i][j]

im1 = np.array(final, dtype=np.uint8)

titles = ['Original Image', 'result of contrast stretching ']
images = [img, im1]

no = 2
for k in range(no):
    plt.subplot(1, no, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()

for i in range(len(images)):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
