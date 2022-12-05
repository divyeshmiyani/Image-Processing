import cv2
import matplotlib.pyplot as plt
import numpy as np

# imgpath = "Fig0504(i)(salt-pepper-noise).tif"
imgpath = "Fig0514(a)(ckt_saltpep_prob_pt25).tif"

img = cv2.imread(imgpath, 0)

cv2.imshow("Original Image", img)

recovered_img = cv2.medianBlur(img, 3)
# recovered_img = cv2.medianBlur(recovered_img, 3)


cv2.imshow("Recoverd Image", recovered_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
