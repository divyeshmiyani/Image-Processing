# Experiment 5
import cv2
import matplotlib.pyplot as plt
import numpy as np

path = ""
imgpath = path + "cameraman.tif"
img = cv2.imread(imgpath, 0)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
k1 = np.array(np.ones((11, 11), np.float32)) / 121  # average filter
print(k1)  # printing mask

output = cv2.filter2D(img, -1, k1)  # here change mask variable

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(output, cmap='gray')
plt.title('Filtered Image')
plt.show()
