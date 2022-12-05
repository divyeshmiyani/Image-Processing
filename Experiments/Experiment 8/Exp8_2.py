import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img1 = cv2.imread('test.tif', 0)

max_val = np.max(img1)
print('Maximum Intensity in Original Image:', max_val)

prob = 0.1
(nr, nc) = img1.shape

output = np.zeros((nr, nc), dtype='uint8')
thres = 1 - prob

for i in range(nr):
    for j in range(nc):
        rdn = random.random()
        if rdn < prob:
            output[i][j] = 0
        elif rdn > thres:
            output[i][j] = 255
        else:
            output[i][j] = img1[i][j]

max_val = np.max(output)
print('Maximum Intensity in Noisy Image:', max_val)
titles = ['Original Image', 'Noisy Image (Salt & Pepper)']
images = [img1, output]

for k in range(2):
    plt.subplot(2, 2, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
    histr_original = cv2.calcHist([img1], [0], None, [256], [0, 258])
    histr_Noisy_SP = cv2.calcHist([output], [0], None, [256], [0, 258])
    plt.subplot(2, 2, 3)
    plt.plot(histr_original)
    plt.title('Histogram of Test Pattern')
    plt.subplot(2, 2, 4)
    plt.plot(histr_Noisy_SP)
    plt.title('Histogram of Noisy Image (Salt & Pepper)')

plt.show()
