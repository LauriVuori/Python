import cv2
import numpy as np
import Func
def empty(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("K")
cv2.resizeWindow("K", 600,600)
cv2.createTrackbar("len", "K", 1, 100, empty)
cv2.createTrackbar("Dist", "K", 100, 200, empty)

lower_yellow = np.array([8,89,142])
upper_yellow = np.array([87,255,255])
mostX,MostY = 0,0
while True:
    _, frame = cap.read()
    lenght = cv2.getTrackbarPos("len", "K")
    dist = cv2.getTrackbarPos("Dist", "K")
    lenght = lenght / 10000
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    inrange = cv2.inRange(gray, lower_yellow, upper_yellow)
    contours, hierarchy = cv2.findContours(inrange, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(type(contours[0]))
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10000:
            approx = cv2.approxPolyDP(contour, lenght*cv2.arcLength(contour,True), True)
            cv2.drawContours(frame,[approx] ,-1,(0,0,255),3)
    stack = Func.stackImages(0.6,([frame],[inrange]))
    cv2.imshow("dst", stack)
    key = cv2.waitKey(1)
    if key == 27:
        print("break")
        exit()
