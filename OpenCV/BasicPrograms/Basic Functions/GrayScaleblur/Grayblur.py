import cv2 as cv

img = cv.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\Basic Functions\\GrayScaleblur\\test.jpg")

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imgBlur = cv.GaussianBlur(imgGray,(7,7),0)

cv.imshow("gray", imgGray)
cv.imshow("blur", imgBlur)

cv.waitKey(0)