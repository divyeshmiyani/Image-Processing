# Objective: Observed the effect of the following high pass filter on image. (I)Ideal (II)Butterworth (III)Gaussian
import cv2
import numpy as np
import matplotlib.pyplot as plt


def make_mask(name):
    dx = nr
    dy = nc
    radius = int(input('Enter Mask Radius: '))
    mask_butter = np.zeros((2 * nr, 2 * nc))
    mask_gauss = np.zeros((2 * nr, 2 * nc))

    if name == 'ideal':
        mask_ideal = np.zeros((2 * nr, 2 * nc))
        for i in range(1, 2 * nr + 1):
            for j in range(1, 2 * nc + 1):
                dist = np.sqrt(np.power(dx - i, 2) + np.power(dy - j, 2))
                if dist <= radius:
                    mask_ideal[i - 1, j - 1] = 1
        return mask_ideal

    if name == 'butter':
        order = int(input("Enter Filter Order:"))
        for i in range(1, 2 * nr + 1):
            for j in range(1, 2 * nc + 1):
                dist = np.sqrt(np.power(dx - i, 2) + np.power(dy - j, 2))
                mask_butter[i - 1, j - 1] = 1 / (1 + ((dist / radius) ** (2 * order)))
        return mask_butter

    if name == 'gauss':
        for i in range(1, 2 * nr + 1):
            for j in range(1, 2 * nc + 1):
                dist = np.sqrt(np.power(dx - i, 2) + np.power(dy - j, 2))
                mask_gauss[i - 1, j - 1] = np.exp(((dist / radius) ** 2) * (-0.5))
    return mask_gauss


# Main Programm   
# Read, Resize, and Pad the image
img = cv2.imread('chap4_1.tif', 0)
img = cv2.resize(img, (200, 200))
(nr, nc) = img.shape
pad_img = np.zeros((2 * nr, 2 * nc), dtype=np.uint8)
pad_img[0:nr, 0:nc] = img

cv2.imshow('Padded Image', pad_img)
cv2.waitKey(0)
cv2.destroyWindow('Padded Image')

# Fourier transform of an image and its spectrum
f = np.fft.fft2(pad_img)
f = np.fft.fftshift(f)
fabs = np.abs(f)

spectrum = 255 * np.log(fabs + 1) / np.log(np.max(fabs + 1))
spectrum = spectrum.astype(np.uint8)

cv2.imshow('Spectrum', spectrum)
cv2.waitKey(0)
cv2.destroyWindow('Spectrum')

# Filter selesction and Mask generation
mask_name = input('Enter ideal, butter or gauss :')
mask = 1 - make_mask(mask_name)
mask = 255 * mask
mask = mask.astype(np.uint8)

cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyWindow('Mask')

cut_spectrum = f * (mask / 255)

# Inverse Fourier transform
back_img = np.abs(np.fft.ifft2(np.fft.fftshift(cut_spectrum)))
out_img = 255 * (back_img / np.max(back_img))
out_img = out_img.astype(np.uint8)

cv2.imshow('Filtered Image', out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

outpath = "filtered_image.png"
cv2.imwrite(outpath, out_img[0:nr, 0:nc])

# Plot the images 
titles = ['Input Image', 'Freq Spectrum', 'HPF Mask, Radius 30', 'Filtered Image']
images = [img, spectrum, mask, out_img[0:nr, 0:nc]]

for k in range(4):
    plt.subplot(1, 4, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()
