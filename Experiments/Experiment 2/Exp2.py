# 4
"""
import cv2
import matplotlib.pyplot as plt
imgpath1 = "1.jpg"
imgpath2 = "2.jpg"
imgpath3 = "3.jpg"
img1 = cv2.imread(imgpath1, 0)
img2 = cv2.imread(imgpath2, 0)
img3 = cv2.imread(imgpath3, 0)
titles = ['Gray Image1', 'Gray Image2', 'Gray Image3']

images = [img1, img2, img3]
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

"""

# 5
'''
import cv2 
imgpath = "./4.png"
img = cv2.imread(imgpath)# ‘0’ is for gray scale image 
# accessing RED value 
X=img.item((10,10,2)) 
print('x:', X) 
# modifying RED value 
img.itemset((10,10,2),100) 
y=img.item(10,10,2) 
print('y:', y)


cv2.imshow("Red", img)
cv2.waitKey(0)
#img[:,:,0] = 255
#img[:,:,2] = 0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i,j,0),255)
        img.itemset((i,j,2),0)



cv2.imshow("Blue", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
import cv2 
import numpy as np

imgpath1 = "./4.png" 
img1 = cv2.imread(imgpath1, 1) 
cv2.imshow('Color Image', img1) 
#cv2.waitKey(0) 
cv2.destroyWindow('Color Image') 
gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY) 
cv2.imshow('Gray Image', gray1) 
#cv2.waitKey(0) #Wait until key strike from keyboard 
cv2.destroyWindow('Gray Image')#Close window

blank = np.zeros((256,512,3), dtype='uint8')

blank[:,:,2] = 255

cv2.imshow('RED', blank)
cv2.waitKey(0) #Wait until key strike from keyboard 
cv2.destroyWindow('RED')#Close window
'''

# 6
'''
import cv2 
import matplotlib.pyplot as plt 
imgpath1 = "1.jpg"
img1 = cv2.imread(imgpath1, 1) 
cv2.imshow('Original Image', img1) 
cv2.waitKey(0) 
(row1,column1,temp) = img1.shape # to access row and column of image 
row2=1500
column2=1500
img2=cv2.resize(img1,(row2,column2), cv2.INTER_AREA)#bilinear interpolation, INTER_NEAREST, INTER_CUBIC
cv2.imshow('Resized Image', img2) 
cv2.waitKey(0) 
print('Original Image Size:',img1.shape) 
print('Resize Image Size:',img2.shape) 
cv2.destroyAllWindows()
'''

import cv2
import matplotlib.pyplot as plt

imgpath1 = r"lena_color_256.tif"
img1 = cv2.imread(imgpath1, 0)

cv2.imshow('Original Image', img1)
cv2.waitKey(0)

(row1, column1) = img1.shape  # to access row and column of image

row2 = 1024
column2 = 1024

img2_inter_near = cv2.resize(img1, (row2, column2),
                             cv2.INTER_NEAREST)  # bilinear interpolation, INTER_NEAREST, INTER_CUBIC
cv2.imshow('Near Image', img2_inter_near)
# cv2.waitKey(0)

img2_inter_cubic = cv2.resize(img1, (row2, column2), cv2.INTER_CUBIC)
cv2.imshow('Cubic Image', img2_inter_cubic)
cv2.waitKey(0)

print('Original Image Size:', img1.shape)
print('Resize Image Size:', img2_inter_near.shape)

cv2.destroyAllWindows()
