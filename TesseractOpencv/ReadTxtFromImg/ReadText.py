import cv2 
import pytesseract
import numpy as np
import stackmodule as stack
import timeit
import Func
#Put tesseract ocr on path 
#pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)


cv2.createTrackbar("Gray min", "Trackbars", 90, 255, nothing)
cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)
"""
cv2.createTrackbar("kernelmin", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("kernelmax", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("morphopenmin", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("morphopenmax", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("morphclosemin", "Trackbars", 20, 30, nothing)
cv2.createTrackbar("morphclosemax", "Trackbars", 20, 30, nothing)
"""
#frame = cv2.imread("kboard.jpg")
cv2.namedWindow("Stacked", cv2.WINDOW_NORMAL) 


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1088)
#adaptivetreshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 11)
TimeCounter = 0
TimerSum2 = 0
Progtimer = 0
while True:
    _, frame = cap.read()
    StartTime = cv2.getTickCount()

    hFrame, wFrame, _ = frame.shape
    g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
    g_max = cv2.getTrackbarPos("Gray max", "Trackbars")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, thresh = cv2.threshold(blurred, g_min, g_max, cv2.THRESH_BINARY)
    maskrange = cv2.inRange(thresh, g_min, g_max)
    e1 = cv2.getTickCount()
    e2 = cv2.getTickCount()
    
    boxes = pytesseract.image_to_boxes(frame)
    for b in boxes.splitlines():
        b = b.split(' ')
        #all strings -> int
    
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(frame,(x,hFrame-y),(w,hFrame-h),(0,0,255),4)
        cv2.putText(frame, b[0], (x, hFrame-y+125), cv2.FONT_HERSHEY_COMPLEX, 5, (50,50,255), 1)
    
    StopTime = cv2.getTickCount()
    TimeCounter += 1
    Progtimer += (StopTime-StartTime)/cv2.getTickFrequency()
    TimerSum2 += (e2 - e1)/cv2.getTickFrequency()
    #stack = Func.stackImages(1,([frame],[maskrange]))
   
    cv2.imshow("Stacked", frame)
    key = cv2.waitKey(1)
    if key == 27:
        print("Average execution time is:", (Progtimer/TimeCounter), "s")
        print("Percent of program execution is:", (TimerSum2/TimeCounter)/(Progtimer/TimeCounter)*100,"%")
        print("break")
        cv2.destroyAllWindows()
        break
#imgStack = stack.stackImages(1,([frame],[frame]))

