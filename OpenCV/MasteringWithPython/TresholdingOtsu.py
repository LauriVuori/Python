import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func
def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)
cv2.createTrackbar("Arc len", "Trackbars", 74, 100, nothing)

image = cv2.imread('keyboard.jpg')
smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
sharpen_image = Func.unsharped_filter(smooth_image_bf)
gray_image = cv2.cvtColor(sharpen_image, cv2.COLOR_BGR2GRAY)


ret1, th1 = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
gray_image_blurred = cv2.GaussianBlur(gray_image, (25, 25), 0)
ret2, th2 = cv2.threshold(gray_image_blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret1, th3 = cv2.threshold(gray_image, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
ret1, th1 = cv2.threshold(th3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

while True:
    a_len = cv2.getTrackbarPos("Arc len", "Trackbars")
    a_len = a_len / 10000
    for contour in contours:
        approx = cv2.approxPolyDP(contour, a_len*cv2.arcLength(contour,True), True)
        cv2.drawContours(image,[approx], -1,(0,0,255),3)
    image_stack = Func.stackImages(0.17,([image,th2,th3],[th1,th2,th3]))
    cv2.imshow("Stack",image_stack)
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
        break