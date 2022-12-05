import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "test.tif"
img1 = cv2.imread(imgpath, 0)

max_val = np.max(img1)
print(max_val)

img2 = (img1 / max_val)  # Normalization

a = 0
b = 0.2
(nr, nc) = img1.shape

x = a + (b * np.random.normal(a, b, (nr, nc)))  # Gaussian Distribution with mean (a) and variance (b)
y = a + ((b - a) * np.random.rand(nr, nc))  # Uniform Distribution

img_guassian = (img2 + x) * max_val
img_guassian_uint8 = np.array(img_guassian, dtype=np.uint8)

img_uniform = (img2 + y) * max_val
img_uniform_uint8 = np.array(img_uniform, dtype=np.uint8)

titles = ['Original Image', 'Noisy Image (Gaussian)', 'Noisy Image (Uniform)']
images = [img1, img_guassian, img_uniform]

for k in range(3):
    plt.subplot(2, 3, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
    histr_original = cv2.calcHist([img1], [0], None, [256], [0, 255])
    histr_Noisy_Gaussian = cv2.calcHist([img_guassian_uint8], [0], None, [256], [0, 255])
    histr_Noisy_Uniform = cv2.calcHist([img_uniform_uint8], [0], None, [256], [0, 255])
    plt.subplot(2, 3, 4)
    plt.plot(histr_original)
    plt.title('Histogram of Test Pattern')
    plt.subplot(2, 3, 5)
    plt.plot(histr_Noisy_Gaussian)
    plt.title('Histogram of Noisy Image (Gaussian)')
    plt.subplot(2, 3, 6)
    plt.plot(histr_Noisy_Uniform)
    plt.title('Histogram of Noisy Image (Uniform)')

plt.show()
