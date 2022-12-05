import cv2

imgpath1 = "Fig07.tif"
img1 = cv2.imread(imgpath1, 1)
cv2.imshow("Img", img1)

(nr, nc, p) = img1.shape
print('\nDimensions of color image')
print('Number of Rows', nr)
print('Number of Rows', nc)
print('Number of colors', p)

cv2.waitKey(0)

img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
cv2.imshow("Img", img2)

(nr, nc) = img2.shape
print('\nDimensions of Grey image')
print('Number of Rows', nr)
print('Number of Rows', nc)

cv2.waitKey(0)
cv2.destroyAllWindows()
