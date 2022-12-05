# 2

from matplotlib import pyplot as plt
import cv2

im = cv2.imread('livingroom.tif', 0)
c = 1
im = im / 255.0
im1 = c * cv2.pow(im, 1.6)
im2 = c * cv2.pow(im, 0.4)
im3 = c * cv2.pow(im, 0.3)

titles = ['Original Image', 'Gamma=0.6', 'Gamma=0.4', 'Gamma=0.3']
images = [im, im1, im2, im3]

for k in range(4):
    plt.subplot(1, 4, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()

for i in range(len(images)):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
