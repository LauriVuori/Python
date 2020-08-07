import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\ResizingCropping\\edge.png")
img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

#(433L=height, 577L=width, 3L=channels)
print(img.shape)

#resize(src, dsize)
imgResize = cv.resize(img, (300,300))
print(imgResize.shape)
#height, width
imgCropped = img[0:200,200:300]

#cv.imshow("image", img)
#cv.imshow("imageres", imgResize)
cv.imshow("Crop", imgCropped)

cv.waitKey(0)