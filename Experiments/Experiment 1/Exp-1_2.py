import cv2

imgpath1 = "Fig03.tif"
img1 = cv2.imread(imgpath1, 0)
(nr, nc) = img1.shape

print('Number of Rows', nr)
print('Number of Rows', nc)

type(img1)
print('Image Data Type: ', img1.dtype)
print('Row Column: ', img1.shape)
print('Dimension : ', img1.ndim)
print('Image Size: ', img1.size)
