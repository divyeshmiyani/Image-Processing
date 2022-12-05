import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Fig0637(a)(caster_stand_original).tif", 1)

cv2.imshow('Original Color Image', img1)

b, g, r = cv2.split(img1)

# b = b*0

rgb_img = cv2.merge([b, g, r])

cv2.imshow('Color Image', rgb_img)
cv2.imshow('Blue Component', b)
cv2.imshow('Green Component', g)
cv2.imshow('Red Component', r)
cv2.waitKey(0)

titles = ['RED Component', 'GREEN Component', 'BLUE Component']
images = [r, g, b]

for k in range(3):
    plt.subplot(1, 3, k + 1)
    plt.imshow(images[k], cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
cv2.destroyAllWindows()
plt.show()
