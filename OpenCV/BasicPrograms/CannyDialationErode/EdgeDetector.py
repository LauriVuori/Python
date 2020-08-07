import cv2 as cv
import numpy as np
#define kernel
kernel = np.ones((5,5),np.uint8)

#read file to img
img = cv.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\EdgeDetector\\edge.png")
img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
#gray image
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#blur gray image
imgBlur = cv.GaussianBlur(imgGray,(7,7),0)

# def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
imgCanny = cv.Canny(img, 150, 250  )

#dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None, /) -> dst
imgDialation = cv.dilate(imgCanny, kernel, iterations=1)

#erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None, /) -> ds
imgEroded = cv.erode(imgDialation, kernel, iterations=1)
#cv.imshow("gray", imgGray)
#cv.imshow("blur", imgBlur)
#cv.imshow("Canny", imgCanny)
#cv.imshow("Dialation", imgDialation)
cv.imshow("Erode", imgEroded)
cv.waitKey(0)