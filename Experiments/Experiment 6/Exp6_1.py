import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath = "Fig0338(a)(blurry_moon).tif"
img = cv2.imread(imgpath, 1)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# k2 = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32) #sharpening filter
# k2 = np.array(([-1, 0, -1], [0,  5, 0], [-1, 0, -1]), np.float32)
k2 = np.array(([-1, -1, -1], [-1, 9, -1], [-1, -1, -1]), np.float32)

print(k2)  # printing mask

sharped_img = cv2.filter2D(img, -1, k2)  # here change mask variable

cv2.imshow("Original Image", img)
cv2.imshow("Sharped Image with Laplacian Filter", sharped_img)
cv2.waitKey(0)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')

plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(sharped_img)
plt.title('Filtered Image')

plt.xticks([])
plt.yticks([])

plt.show()

cv2.destroyAllWindows()
