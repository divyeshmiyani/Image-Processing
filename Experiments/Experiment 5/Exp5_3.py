import cv2
import matplotlib.pyplot as plt
import numpy as np

# imgpath = "Fig0504(i)(salt-pepper-noise).tif"
imgpath = "Fig0514(a)(ckt_saltpep_prob_pt25).tif"

img = cv2.imread(imgpath, 0)

cv2.imshow("Original Image", img)

k1 = np.array(np.ones((3, 3), np.float32))

img_recovered_with_avg_filter = cv2.filter2D(img, -1, k1)
img_recovered_with_median_filter = cv2.medianBlur(img, 3)

cv2.imshow("Image Recoverd with Median Filter", img_recovered_with_median_filter)
cv2.imshow("Image Recoverd with Average Filter", img_recovered_with_avg_filter)
cv2.waitKey(0)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(img_recovered_with_avg_filter, cmap='gray')
plt.title('Avg Filter')

plt.subplot(1, 3, 3)
plt.imshow(img_recovered_with_median_filter, cmap='gray')
plt.title('Median Filter')

plt.show()

cv2.destroyAllWindows()
