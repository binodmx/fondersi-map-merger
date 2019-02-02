import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.png')

for row in img:
    for col in row:
        if col[0] < 255:
            col[0] = 255
            col[1] = 0
            col[2] = 0
            
cv2.imwrite('image.png',img)
