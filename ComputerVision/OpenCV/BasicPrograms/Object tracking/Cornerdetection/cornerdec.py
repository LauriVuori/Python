import cv2
import stackmodule as stack
import numpy as np
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)

def nothing(x):
    pass

cv2.createTrackbar("Gray min", "Trackbars", 66, 255, nothing)
cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Arc len", "Trackbars", 74, 100, nothing)


cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    _, frame = cap.read()
    g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
    g_max = cv2.getTrackbarPos("Gray max", "Trackbars")
    a_len = cv2.getTrackbarPos("Arc len", "Trackbars")
    a_len = a_len / 10000
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blurred, g_min, g_max, cv2.THRESH_BINARY_INV)
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)

    test = cv2.bitwise_or(thresh,thresh1)
    #res1 = cv2.bitwise_and(frame,frame,mask=thresh)



    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, a_len*cv2.arcLength(contour,True), True)
        cv2.drawContours(frame,[approx] ,-1,(0,0,255),3)
    imgStack = stack.stackImages(0.2,([test,thresh,],[thresh2, thresh3],[thresh4,thresh5]))
    cv2.imshow("Stacked", imgStack)
    key = cv2.waitKey(1)
    if key == 27: #esc
        cv2.destroyAllWindows()
        break