# Objective: Plot the specturm of an Image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('chap4_4.tif', 0)
# img = cv2.resize(img,(500,500))

(nr, nc) = img.shape
cv2.imshow('Original Image', img)
cv2.waitKey(0)

# Fourier transform of an image and its spectrum
f = np.fft.fft2(img)
f = np.fft.fftshift(f)
f_abs = np.abs(f)

cv2.imshow('Spectrum with out LOG trasform', f_abs)
cv2.waitKey(0)

spectrum = 255 * np.log(f_abs + 1) / np.log(np.max(f_abs + 1))
spectrum = spectrum.astype(np.uint8)

cv2.imshow('Spectrum', spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()
