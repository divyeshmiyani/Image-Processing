import cv2

imgpath1 = "Fig07.tif"
img1 = cv2.imread(imgpath1, 1)
cv2.imshow("Img", img1)

(nr, nc, p) = img1.shape

print('Number of Rows', nr)
print('Number of Rows', nc)
print('Number of colors', p)

cv2.waitKey(0)
cv2.destroyAllWindows()
