from PIL import ImageGrab
import numpy as np
import cv2
def empty(x):
    pass
cv2.namedWindow("Tbars")
cv2.resizeWindow("Tbars", 600,600)
cv2.createTrackbar("Hue min", "Tbars", 47, 179, empty)
cv2.createTrackbar("Hue max", "Tbars", 127, 179, empty)

cv2.createTrackbar("Sat min", "Tbars", 168, 255, empty)
cv2.createTrackbar("Sat max", "Tbars", 255, 255, empty)

cv2.createTrackbar("Val min", "Tbars", 91, 255, empty)
cv2.createTrackbar("Val max", "Tbars", 158, 255, empty)


print("1)Mining\n2)Archeology")
Skill = int(input())
if Skill == 1:
    
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
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(frame,lower,upper)
        # contours, hierarchy = cv2.findContours(mask, )
        
        cv2.imshow("test", frame)
        cv2.imshow("t", mask)
        k = cv2.waitKey(1)
        if k == 27:
            cv2.destroyAllWindows()
            exit()