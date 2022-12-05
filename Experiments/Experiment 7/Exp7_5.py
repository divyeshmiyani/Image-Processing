import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Fig0505(a)(applo17_boulder_noisy).tif', 0)
img = cv2.resize(img, (500, 500))
cv2.imshow('Original Image', img)
cv2.waitKey(0)

(nr, nc) = img.shape

# Fourier transform of an image and its spectrum
f = np.fft.fft2(img)
f = np.fft.fftshift(f)
f_abs = np.abs(f)
# cv2.imshow('Spectrum with out LOG trasform', f_abs)
# cv2.waitKey(0)

spectrum = 255 * np.log(f_abs + 1) / np.log(np.max(f_abs + 1))
spectrum = spectrum.astype(np.uint8)
cv2.imshow('Spectrum', spectrum)
cv2.waitKey(0)

mask = np.ones((500, 500))
mask[0:244, 244:255] = 0
mask[254:nr, 244:255] = 0

cv2.imshow('Mask', mask)
cv2.waitKey(0)

# To Observe noise
# add one result in Journal of noise
# mask = 1-mask

cut_spectrum = f * mask
# Inverse Fourier transform
back_img = np.abs(np.fft.ifft2(np.fft.fftshift(cut_spectrum)))
out_img = 255 * (back_img / np.max(back_img))
out_img = out_img.astype(np.uint8)
cv2.imshow('Filtered Image', out_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
