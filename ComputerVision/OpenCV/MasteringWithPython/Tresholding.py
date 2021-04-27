import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func
def nothing(x):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)
cv2.createTrackbar("Gray val", "Trackbars", 0, 255, nothing)

image = cv2.imread('keyboard.jpg')
smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
sharpen_image = Func.unsharped_filter(smooth_image_bf)
gray_image = cv2.cvtColor(sharpen_image, cv2.COLOR_BGR2GRAY)


while True:
    grayval = cv2.getTrackbarPos("Gray val", "Trackbars")
    ret1, thresh1 = cv2.threshold(gray_image, grayval+10, 255, cv2.THRESH_BINARY)
    ret2, thresh2 = cv2.threshold(gray_image, grayval+20, 255, cv2.THRESH_BINARY)
    ret3, thresh3 = cv2.threshold(gray_image, grayval+30, 255, cv2.THRESH_BINARY)
    ret4, thresh4 = cv2.threshold(gray_image, grayval+40, 255, cv2.THRESH_BINARY)
    ret5, thresh5 = cv2.threshold(gray_image, grayval+50, 255, cv2.THRESH_BINARY)
    ret6, thresh6 = cv2.threshold(gray_image, grayval+60, 255, cv2.THRESH_BINARY)
 
    print("tresh1:",grayval+10,"tresh2:",grayval+20,"tresh3:",grayval+30,"tresh4:",grayval+40)
    print("tresh5:",grayval+50,"tresh6:",grayval+60)
    image_stack = Func.stackImages(0.17,([thresh1,thresh2,thresh3],[thresh4,thresh5,thresh6]))
    cv2.imshow("Stack",image_stack)
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
        break