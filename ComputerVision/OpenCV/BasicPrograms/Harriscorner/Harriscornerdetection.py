import cv2
import numpy as np
import Func
def empty(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("K")
cv2.resizeWindow("K", 600,600)
cv2.createTrackbar("Corner", "K", 1, 100, empty)
cv2.createTrackbar("Dist", "K", 1, 100, empty)

lower_yellow = np.array([8,89,142])
upper_yellow = np.array([87,255,255])

while True:
    _, frame = cap.read()
    corner = cv2.getTrackbarPos("Corner", "K")
    dist = cv2.getTrackbarPos("Dist", "K")
    corner = corner /100
    dist = dist/100
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    inrange = cv2.inRange(gray, lower_yellow, upper_yellow)
    gray = np.float32(inrange)

    dst = cv2.cornerHarris(gray, 5, 3, corner)


    frame[dst> dist*dst.max()] = [0,0,255]
    stack = Func.stackImages(0.6,([frame],[gray]))
    cv2.imshow("dst", stack)
    key = cv2.waitKey(1)
    if key == 27:
        print("break")
        exit()
