# Objective: Remove DC component from the spectrum and observed the effect on recovered image.

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
f1 = np.fft.fftshift(f)
f_abs = np.abs(f1)

spectrum = 255 * np.log(f_abs + 1) / np.log(np.max(f_abs + 1))
spectrum = spectrum.astype(np.uint8)
cv2.imshow('Spectrum', spectrum)
cv2.waitKey(0)

f[0, 0] = 0  # Make DC component Zero
# Inverse Fourier transform
back_img = np.abs(np.fft.ifft2(f))
out_img = 255 * (back_img / np.max(back_img))
out_img = out_img.astype(np.uint8)
cv2.imshow('Filtered Image', out_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
