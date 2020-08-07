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


#for color video only
"""
cv2.createTrackbar("Hue min", "Trackbars", 23, 180, nothing)
cv2.createTrackbar("Hue max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Sat min", "Trackbars", 100, 255, nothing)
cv2.createTrackbar("Sat max", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("Val min", "Trackbars", 233, 255, nothing)
cv2.createTrackbar("Val max", "Trackbars", 255, 255, nothing)
"""
cv2.createTrackbar("Gray min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)
#cv2.createTrackbar("Tresh min", "Trackbars", 0, 255, nothing)
#cv2.createTrackbar("Tresh max", "Trackbars", 255, 255, nothing)

cv2.createTrackbar("Arc len", "Trackbars", 2, 100, nothing)
cv2.createTrackbar("Area", "Trackbars", 454, 1000, nothing)

#if video
cap = cv2.VideoCapture(0)

#if picture
#cap = cv2.imread('edge.png')

while True:
    # if video
    _, frame = cap.read()


    #if pic
    #frame = cap
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


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

    #Get positions of sliders
    a_len= cv2.getTrackbarPos("Arc len", "Trackbars")
    
    a_len = a_len /100
    area_s = cv2.getTrackbarPos("Area", "Trackbars")

    #Get gray values from sliders
    g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
    g_max = cv2.getTrackbarPos("Gray max", "Trackbars")
    
    
    #Video transformations
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Get treshold values from sliders
    ret, thresh = cv2.threshold(gray, g_min, g_max, cv2.THRESH_BINARY_INV)

    blurred = cv2.GaussianBlur(thresh, (5, 5), 0)
    #thresh = cv2.threshold(blurred, t_min, t_max, cv2.THRESH_BINARY)[1]
    
    
    mask = cv2.inRange(blurred,g_min,g_max)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    
    #contours detection
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area = cv2.contourArea(cnt)
        #change 0.1*cv2.archL.... 
        approx = cv2.approxPolyDP(cnt, a_len*cv2.arcLength(cnt,True), True)
        
        #Detected object area vs slider area
        if area > area_s:
            #Draw contours on frame
            cv2.drawContours(thresh, [approx], 0, [0,255,0], 4)

            #TODO: Look up explanation approx.ravel, get coordinates contour
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            #print(len(approx))

            # Write X and Y coordinates to detected object
            if len(approx) >= 150:
                XandY = str(x)+", "+str(y)
                cv2.putText(frame, XandY , (x,y), font, 2, (0,0,255)) 

    #Video     
    #cv2.imshow("Frame", frame)
    #cv2.imshow("Mask",mask)


    #if pic
    #imgResult = cv2.bitwise_and(cap,cap,mask=mask)




    #Stack images, just for convenience
    imgStack = stck.stackImages(0.6,([frame,gray,thresh]))
    cv2.imshow("Stacked", imgStack)
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss * pow(10, -6)
    print("%0.2f" %memory)  # in bytes 

    key = cv2.waitKey(1)
    if key == 27: #esc
        break

 

cap.release()
cv2.destroyAllWindows()