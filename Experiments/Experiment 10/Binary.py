import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('coins.png', 0)

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histogram)
plt.show()

threshold = 100
output = []

for i in img:
    row = []
    for pixel in i:
        pxl = 255 if pixel > threshold else 0
        row.append(pxl)
    output.append(row)

output = np.array(output, dtype=np.uint8)

cv2.imshow("Original Image", output)
cv2.waitKey(0)

cv2.destroyAllWindows()
