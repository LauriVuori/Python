import cv2
import numpy as np
import stackmodule as stck #Module for stacking windows
import imutils
import psutil
import math
import os

def nothing(x):
    pass

font = cv2.FONT_HERSHEY_COMPLEX

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)

cv2.createTrackbar("Gray min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)
#cv2.createTrackbar("Tresh min", "Trackbars", 0, 255, nothing)
#cv2.createTrackbar("Tresh max", "Trackbars", 255, 255, nothing)

cv2.createTrackbar("Arc len", "Trackbars", 2, 100, nothing)
cv2.createTrackbar("Area", "Trackbars", 454, 1000, nothing)


img = cv2.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\Projects\\Keyboardtracking\\edge.png")


while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Get positions of sliders
    a_len= cv2.getTrackbarPos("Arc len", "Trackbars")    
    a_len = a_len /100
    area_s = cv2.getTrackbarPos("Area", "Trackbars")
    #Get gray values from sliders
    g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
    g_max = cv2.getTrackbarPos("Gray max", "Trackbars")
    
    

    #Get treshold values from sliders
    ret, thresh = cv2.threshold(gray, g_min, g_max, cv2.THRESH_BINARY_INV)

    blurred = cv2.GaussianBlur(thresh, (5, 5), 0)
    #thresh = cv2.threshold(blurred, t_min, t_max, cv2.THRESH_BINARY)[1]
    
    
    mask = cv2.inRange(blurred,6,255)
    res = cv2.bitwise_and(img,img, mask= mask)

    
    #contours detection
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #Stack images, just for convenience

    key = cv2.waitKey(1)
    if key == 27: #esc
        break

def getContours(img):
    #retrieves extreme outer contours 
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]   
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>10:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h= cv2.boundingRect(approx)

            if objCor ==3:objectType = "Tri"
            elif objCor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType="Square"
                else:objectType="Rectangle"
            elif objCor > 4: objectType="Circle"
            else:objectType="None"
            #draw rectangles on objects
            cv2.rectangle(imgContour, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.8,
                        (0,0,0),2)

    imgCanny = cv2.Canny(img, 50, 50)
    imgStack = stck.stackImages(0.6,([img,imgCanny], [thresh, thresh]))
    
    cv2.imshow("Stacked", imgStack)

 

img.release()
cv2.destroyAllWindows()


    #HSV COLOR PICTURE ONLY, Detecting colors
"""
    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min= cv2.getTrackbarPos("Val min", "Trackbars")
    v_max= cv2.getTrackbarPos("Val max", "Trackbars")

    #t_min = cv2.getTrackbarPos("Tresh min", "Trackbars")
    #t_max = cv2.getTrackbarPos("Tresh max", "Trackbars")
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
"""
    #for color video only
"""
cv2.createTrackbar("Hue min", "Trackbars", 23, 180, nothing)
cv2.createTrackbar("Hue max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Sat min", "Trackbars", 100, 255, nothing)
cv2.createTrackbar("Sat max", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("Val min", "Trackbars", 233, 255, nothing)
cv2.createTrackbar("Val max", "Trackbars", 255, 255, nothing)
"""