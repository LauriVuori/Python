import cv2
import time
import stackmodule as stack
import numpy as np
import pytesseract


def Trackbars():
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 600,600)
    cv2.createTrackbar("Gray min", "Trackbars", 66, 255, nothing)
    cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)


def nothing(x):
    pass

def opencamera():
    cap = cv2.VideoCapture(0)
    return cap
    

def FrameMasking(image, min_val, max_val):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #tresholds
    ret, thresh = cv2.threshold(blurred, min_val, max_val, cv2.THRESH_BINARY_INV)
    #maskrange = cv2.inRange(thresh, min_val, max_val)
    return thresh

    
            

while True:
    Trackbars()
    #frame = cv2.imread("test.png")
    #if cap.isOpened():
    command = input("Read pic y/n?")
    #while True:
    if command == 'y':
        cap = opencamera()
        _, frame = cap.read()
        #frame = cap.read()
        g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
        g_max = cv2.getTrackbarPos("Gray max", "Trackbars")
        MaskedFrame = FrameMasking(frame, g_min, g_max)
        
        hFrame, wFrame, _ = frame.shape
        frame = MaskedFrame
        boxes = pytesseract.image_to_boxes(frame)
        for b in boxes.splitlines():
            b = b.split(' ')
            print(b[0][0])
            #print(b)
            #all strings -> int
            x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(frame,(x,hFrame-y),(w,hFrame-h),(0,0,255),1)
            cv2.putText(frame, b[0], (x, hFrame-y+125), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,255),1)
        
        
        while True:
            imgStack = stack.stackImages(0.5,([frame,frame],[MaskedFrame,MaskedFrame]))
            cv2.imshow("Stacked", imgStack)
            key = cv2.waitKey(1)
            if key == 27:
                print("break")
                cap.release()
                break
