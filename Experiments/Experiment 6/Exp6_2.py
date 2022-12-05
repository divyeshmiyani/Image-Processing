import cv2
# Load the image
image = cv2.imread("cameraman.tif", 0)

# Blur the image
gauss = cv2.GaussianBlur(image, (7,7), 0)

# Apply Unsharp masking
unsharp_image = cv2.addWeighted(image, 2, gauss, -1, 0)

# Apply HighBoost masking
highboost_image = cv2.addWeighted(image, 4, gauss, -1, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', gauss)
cv2.imshow('Unsharped Image', unsharp_image)
cv2.imshow('HighBoost Image', highboost_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
