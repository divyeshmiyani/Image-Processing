from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('livingroom.tif', 0)

img_log = (np.log(img + 1) / (np.log(1 + np.max(img)))) * 255
img_log1 = np.array(img_log, dtype=np.uint8)

titles = ['Original Image', 'log_image']
images = [img, img_log1]

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
