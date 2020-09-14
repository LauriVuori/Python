from PIL import ImageGrab
import numpy as np
import cv2
def empty(x):
    pass
cv2.namedWindow("Tbars")
cv2.resizeWindow("Tbars", 600,600)
cv2.createTrackbar("Hue min", "Tbars", 104, 179, empty)
cv2.createTrackbar("Hue max", "Tbars", 148, 179, empty)

cv2.createTrackbar("Sat min", "Tbars", 86, 255, empty)
cv2.createTrackbar("Sat max", "Tbars", 221, 255, empty)

cv2.createTrackbar("Val min", "Tbars", 78, 255, empty)
cv2.createTrackbar("Val max", "Tbars", 255, 255, empty)


# print("1")
# Skill = int(input())
# if Skill == 1:
    
while(True):
    h_min = cv2.getTrackbarPos("Hue min", "Tbars")
    h_max = cv2.getTrackbarPos("Hue max", "Tbars")
    s_min = cv2.getTrackbarPos("Sat min", "Tbars")
    s_max = cv2.getTrackbarPos("Sat max", "Tbars")
    v_min = cv2.getTrackbarPos("Val min", "Tbars")
    v_max = cv2.getTrackbarPos("Val max", "Tbars")
    
    img = ImageGrab.grab(bbox=(0,0,1980,1240)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    frame = img_np
    img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_np,lower,upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if (area > 500):
            print(area)
            # x,y,w,h = cv2.boundingRect(contour)
            # approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour,True), True)
            cv2.drawContours(frame,[contour] ,-1,(0,0,255),3)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame,[box],0,(0,255,0),2)
            # ObjCorners = len(approx)
    
    cv2.imshow("test", frame)
    # cv2.imshow("t", mask)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()