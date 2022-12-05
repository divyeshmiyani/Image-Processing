import cv2

imgpath1 = "Fig03.tif"
imgpath2 = "Fig04.tif"
imgpath3 = "Fig05.tif"
img1 = cv2.imread(imgpath1, 0)
img2 = cv2.imread(imgpath2, 0)
img3 = cv2.imread(imgpath3, 0)
cv2.imshow("Chest", img1)
cv2.waitKey(0)
cv2.imshow("X-ray", img2)
cv2.waitKey(0)
cv2.imshow("Img", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
