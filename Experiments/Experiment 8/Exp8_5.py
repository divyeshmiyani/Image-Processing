import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

imgpath = "test2.tif"
img1 = cv2.imread(imgpath, 0)

(nr, nc) = img1.shape

# Adding Salt&Pepper Noise
prob = 0.05

R = np.zeros((nr, nc), dtype='uint8')
thres = 1 - prob

for i in range(nr):
    for j in range(nc):
        rdn = random.random()
        if rdn < prob:
            R[i][j] = 0
        #   if rdn > thres:
        #        R[i][j]=255;
        else:
            R[i][j] = img1[i][j]

img_noise = R

###### Contra-Harmonic Filter
(nr, nc) = img_noise.shape  # to access row and column of image
print('No. of Row: ', nr)
print('No. of Column: ', nc)
output = np.zeros((nr, nc), dtype='uint8')
Q = 0.5
for i in range(1, nr - 1, 1):
    for j in range(1, nc - 1, 1):
        num = 0
        denom = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                num = num + (pow(img_noise[x][y], (Q + 1)))
                denom = denom + (pow(img_noise[x][y], Q))
        if denom != 0:
            output[i][j] = np.uint8(num / denom)

plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 2)
plt.imshow(img_noise, cmap='gray')
plt.title('Noisy Image')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 3)
plt.imshow(output, cmap='gray')
plt.title('Filtered Image')
plt.xticks([])
plt.yticks([])
plt.show()
cv2.waitKey(0)  # Wait until key strike from keyboard
cv2.destroyAllWindows()  # Close all windows
