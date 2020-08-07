#img = cv.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\ResizingCropping\\edge.png")

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\WarpPerspective\\keyboard.jpg")
imgResize = cv2.resize(img, (800,600))

width,height = 800,400
pts1 = np.float32([[66,175],[723,185],[0,301],[797,307]])

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(imgResize, matrix, (width, height))

cv2.imshow("Image", imgOutput)

cv2.waitKey(0)