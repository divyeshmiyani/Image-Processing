import cv2
import numpy as np
import matplotlib.pyplot as plt
import random


def trimmeanval(arr, d):
    n = len(arr)
    k = int(d / 2)
    return np.mean(arr[k:n - k])


img1 = cv2.imread('test.tif', 0)

max_val = np.max(img1)
print(max_val)

img2 = (img1 / max_val)  # Normalization

a = 0
b = 0.05
(nr, nc) = img1.shape

x = a + (b * np.random.normal(a, b, (nr, nc)))  # Gaussian Distribution with mean (a) and variance (b)
y = a + ((b - a) * np.random.rand(nr, nc))  # Uniform Distribution

img_guassian = (img2 + x) * max_val
img_guassian_uint8 = np.array(img_guassian, dtype=np.uint8)

# Adding Salt&Pepper Noise
prob = 0.05

output2 = np.zeros((nr, nc), dtype='uint8')
thres = 1 - prob

for i in range(nr):
    for j in range(nc):
        rdn = random.random()
        if rdn < prob:
            output2[i][j] = 0
        elif rdn > thres:
            output2[i][j] = 255
#        else:
#            output2[i][j]=img_guassian[i][j];

img_guassian_uint8 = np.array(img_guassian, dtype=np.uint8)

# Alpha Trimmed Filter
img_noise = img_guassian + output2
(nr, nc) = img_noise.shape  # to access row and column of image
print('No. of Row: ', nr)
print('No. of Column: ', nc)

recovred_image = np.zeros((nr, nc), dtype='uint8')
ary = np.zeros(9, dtype='uint8')
ary1 = np.zeros(9, dtype='uint8')
d = 4
for i in range(1, nr - 1):
    for j in range(1, nc - 1):
        temp = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                ary[temp] = img_noise[x, y]
                temp += 1
        ary.sort()
        ary1 = ary
        recovred_image[i][j] = trimmeanval(ary, d)

titles = ['Original Image', 'Noisy Image(Gaussian + Salt & Pepper)', 'Recoverd Image']
images = [img1, img_noise, recovred_image]

for k in range(3):
    plt.subplot(2, 3, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
    histr_original = cv2.calcHist([img1], [0], None, [256], [0, 258])
    histr_Noisy_Gaussian = cv2.calcHist([np.uint8(img_noise)], [0], None, [256], [0, 258])
    histr_recovred_image = cv2.calcHist([recovred_image], [0], None, [256], [0, 258])
    plt.subplot(2, 3, 4)
    plt.plot(histr_original)
    plt.title('Histogram of Test Pattern')
    plt.subplot(2, 3, 5)
    plt.plot(histr_Noisy_Gaussian)
    plt.title('Histogram of Noisy Image(Gaussian+Salt & Pepper)')
    plt.subplot(2, 3, 6)
    plt.plot(histr_recovred_image)
    plt.title('Histogram of Recovred Image')

plt.show()
