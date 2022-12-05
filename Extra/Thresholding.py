import cv2
import matplotlib.pyplot as plt
import numpy as np

img = [[99,100,101,102,849,56,15,205,56,0],
[99,100,101,102,89,56,156,205,56,0],
[99,100,101,102,89,56,150,205,56,0],
[99,100,11,102,89,56,155,205,56,0],
[99,100,101,102,89,56,158,205,56,0],
[99,100,101,102,89,56,155,205,56,0],
[99,100,10,102,89,56,152,25,56,0],
[99,100,101,102,89,56,15,20,56,0],
[99,100,101,102,89,56,15,5,56,0],
[99,100,101,2,89,56,15,0,56,0]]
threshold = 100
output = []
for i in img:
    row = []
    for pixel in i:
        pxl = 255 if pixel > threshold else 0
        row.append(pxl)
    output.append(row)

output2 = [[(255 if pixel > threshold else 0) for pixel in i] for i in img]


assert output == output2