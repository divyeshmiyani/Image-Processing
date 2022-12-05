import cv2
import matplotlib.pyplot as plt

imgpath1 = "Fig03.tif"
imgpath2 = "Fig04.tif"
imgpath3 = "Fig05.tif"
img1 = cv2.imread(imgpath1, 0)
img2 = cv2.imread(imgpath2, 0)
img3 = cv2.imread(imgpath3, 0)

images = [img1, img2, img3]
titles = ['Image 1', 'Image2', 'Image3']

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
