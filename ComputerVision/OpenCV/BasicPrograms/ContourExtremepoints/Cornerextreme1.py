import cv2
import numpy as np
import Func
def empty(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("K")
cv2.resizeWindow("K", 600,600)
cv2.createTrackbar("Corner", "K", 1, 100, empty)
cv2.createTrackbar("Dist", "K", 100, 200, empty)

lower_yellow = np.array([8,89,142])
upper_yellow = np.array([87,255,255])

while True:
    _, frame = cap.read()
    corn = cv2.getTrackbarPos("Corner", "K")
    dist = cv2.getTrackbarPos("Dist", "K")

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    inrange = cv2.inRange(gray, lower_yellow, upper_yellow)
    canny = cv2.Canny(inrange,corn, dist)
    corners = cv2.goodFeaturesToTrack(canny, 4, 0.5, 50)
    print(type(corners))
    for corner in corners:

        x,y = corner.ravel()
        cv2.circle(frame,(x,y),5,(36,255,12),-1)
    
    stack = Func.stackImages(0.6,([frame,gray],[canny,frame]))
    cv2.imshow("dst", stack)
    key = cv2.waitKey(1)
    if key == 27:
        print("break")
        exit()
