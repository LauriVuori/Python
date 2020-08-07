import cv2
import numpy as np

def nothing(x):
    pass

font = cv2.FONT_HERSHEY_COMPLEX

cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue min", "Trackbars", 17, 180, nothing)

cv2.createTrackbar("Hue max", "Trackbars", 42, 255, nothing)

cv2.createTrackbar("Sat min", "Trackbars", 94, 255, nothing)

cv2.createTrackbar("Sat max", "Trackbars", 179, 180, nothing)

cv2.createTrackbar("Val min", "Trackbars", 108, 255, nothing)

cv2.createTrackbar("Val max", "Trackbars", 247, 255, nothing)

cv2.createTrackbar("Arc len", "Trackbars", 0, 100, nothing)

cv2.createTrackbar("Area", "Trackbars", 464, 1000, nothing)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min= cv2.getTrackbarPos("Val min", "Trackbars")
    v_max= cv2.getTrackbarPos("Val max", "Trackbars")
    
    a_len= cv2.getTrackbarPos("Arc len", "Trackbars")
    a_len = a_len /100
    
    area_s = cv2.getTrackbarPos("Area", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv,lower,upper)

    #contours detection
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        #change 0.1*cv2.archL....
        approx = cv2.approxPolyDP(cnt, a_len*cv2.arcLength(cnt,True), True)
        
        if area > area_s:
            cv2.drawContours(frame, [approx], 0, [0,0,0], 4)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            #print(len(approx))
            if len(approx) >= 300:
                cv2.putText(frame, "BANANA", (x,y), font, 2, (0,0,255))
        
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1)
    if key == 27: #esc
        break

 

cap.release()
cv2.destroyAllWindows()