import cv2
import numpy as np
import stackmodule as stck #Module for stacking windows


def getContours(img):
    #retrieves extreme outer contours 
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]   
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>2000:
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



cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imgGray,(7,7), 1)
    #canny corners
    imgCanny = cv2.Canny(imgblur, 50, 50)
    getContours(imgCanny)
    k = cv2.waitKey(1) & 0xFF
    imgBlank = np.zeros_like(img)
    imgStack = stck.stackImages(0.6,([img,imgGray,imgblur],
                                [imgCanny,imgContour,imgBlank]))
    cv2.imshow("Stacked", imgStack)
    if k == ord('q'):
        break
