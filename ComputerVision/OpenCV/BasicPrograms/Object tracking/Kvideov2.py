import cv2   
import numpy as np
import stackmodule as stck
import math

def nothing(x):
    pass

font = cv2.FONT_HERSHEY_COMPLEX

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)

cv2.createTrackbar("Gray min", "Trackbars", 66, 255, nothing)
cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Arc len", "Trackbars", 74, 100, nothing)
cv2.createTrackbar("Area", "Trackbars", 50000, 200000, nothing)
"""
cv2.createTrackbar("kernelmin", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("kernelmax", "Trackbars", 5, 30, nothing)

cv2.createTrackbar("morphopenmin", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("morphopenmax", "Trackbars", 5, 30, nothing)
cv2.createTrackbar("morphclosemin", "Trackbars", 20, 30, nothing)
cv2.createTrackbar("morphclosemax", "Trackbars", 20, 30, nothing)
"""

#####################
"""HSV
cv2.createTrackbar("Canny min", "Trackbars", 0, 500, nothing)
cv2.createTrackbar("Canny max", "Trackbars", 500, 500, nothing)
cv2.createTrackbar("Hue min", "Trackbars", 39, 180, nothing)
cv2.createTrackbar("Hue max", "Trackbars", 146, 255, nothing)
cv2.createTrackbar("Sat min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Sat max", "Trackbars", 109, 180, nothing)
cv2.createTrackbar("Val min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Val max", "Trackbars", 90, 255, nothing)
"""
########################



cap=cv2.VideoCapture(0)



vcap = cap
if vcap.isOpened():
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    width  = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    #print(cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT) # 3, 4

    # or
    width = vcap.get(3) # float
    height = vcap.get(4) # float

    print('width, height:', width, height)

    fps = vcap.get(cv2.CAP_PROP_FPS)
    print('fps:', fps)  # float
    # print(cv2.CAP_PROP_FPS) # 5

    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('frames count:', frame_count)  # float
    # print(cv2.CAP_PROP_FRAME_COUNT) # 7

while True:
    d = 0.1
    centers = []
    _, frame = cap.read()


    # Get gray values from sliders
    g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
    g_max = cv2.getTrackbarPos("Gray max", "Trackbars")
    # Get positions of sliders
    a_len = cv2.getTrackbarPos("Arc len", "Trackbars")
    a_len = a_len / 10000
    area_s = cv2.getTrackbarPos("Area", "Trackbars")
    """
    ker_min = cv2.getTrackbarPos("kernelmin", "Trackbars")
    ker_max = cv2.getTrackbarPos("kernelmax", "Trackbars")
    morpopmin = cv2.getTrackbarPos("morphopenmin", "Trackbars")
    morpomax = cv2.getTrackbarPos("morphopenmax", "Trackbars")
    morpcmin = cv2.getTrackbarPos("morphopenmin", "Trackbars")
    morpcmax = cv2.getTrackbarPos("morphclosemax", "Trackbars")
    """
        

    """
    ###Canny
    c_min = cv2.getTrackbarPos("Canny min", "Trackbars")
    c_max = cv2.getTrackbarPos("Canny max", "Trackbars")
    ####

    ################################HSV
    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min= cv2.getTrackbarPos("Val min", "Trackbars")
    v_max= cv2.getTrackbarPos("Val max", "Trackbars")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    maskhsv = cv2.inRange(hsv,lower,upper)
    ###Canny, TODO: useless atm
    canny = cv2.Canny(frame,c_min,c_max)
    """

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    #tresholds
    ret, thresh = cv2.threshold(blurred, g_min, g_max, cv2.THRESH_BINARY_INV)
    maskrange = cv2.inRange(thresh, g_min, g_max)

    #th2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,adaptivemin,adaptivemax)
    #th3 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


    #(mask, maskhsv) (mask, canny), TODO: useless atm
    #res = cv2.bitwise_and(maskrange, maskhsv)

    #Morphological Transformations
    kernel = np.ones((5,5),np.uint8)
    maskerode = cv2.erode(maskrange, kernel, iterations = 1)
    maskdilation = cv2.dilate(maskerode, kernel, iterations = 1)
    maskopen = cv2.morphologyEx(maskdilation, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    maskclose = cv2.morphologyEx(maskopen, cv2.MORPH_CLOSE, np.ones((20, 20), np.uint8))
    
    
    #gray2 = cv2.bitwise_and(frame,frame, mask = thresh)
    #gray2 = cv2.erode(thresh, kernal, iterations=2)



    contours, hierarchy = cv2.findContours(maskclose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #for pic, contour in enumerate(contours):
    for contour in contours:
        area = cv2.contourArea(contour)
        
        """
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, a_len*cv2.arcLength(cnt,True), True)
            cv2.drawContours(frame, [approx], 0, [0,255,0], 4)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            #print(len(approx))

            # Write X and Y coordinates to detected object
            if len(approx) >= 150:
                XandY = str(x)+", "+str(y)
                cv2.putText(frame, XandY , (x,y), font, 2, (0,0,255)) 
        """
        if(area>area_s):
            x,y,w,h = cv2.boundingRect(contour)
            approx = cv2.approxPolyDP(contour, a_len*cv2.arcLength(contour,True), True)
            cv2.drawContours(frame,[approx] ,-1,(0,0,255),3)
            ObjCorners = len(approx)
            """
            rect = cv.minAreaRect(cnt)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            cv.drawContours(img,[box],0,(0,0,255),2)
            """
            #print(ObjCorners)
            if (ObjCorners >= 4) and (ObjCorners <= 50):
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(frame, [box], 0,(0,255,255),2)
                img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(frame,"Keyboard",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
                M = cv2.moments(contour) 
                cx = int(M['m10'] /M['m00'])
                cy = int(M['m01'] /M['m00'])
                #[x,y] akselit
                centers.append([cx, cy])
                cv2.circle(img, (cx, cy), 7, (255, 255, 255), -1)
                location = ""
                location += str(cx)+ "," + str(cy)
                cv2.putText(frame, location, (cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0))
                #Static dot
                #cv2.line(img, tuple(a), tuple(b), (0,255,0),2)
                if len(centers)==1:
                    a = cv2.line(img, tuple(centers[0]), (480,0), (0,255,0),2)
                    ##calculate difference between center and predefined dot
                    #print(centers[0])
                    temp = centers[0]
                    xCenter = temp[0]
                    yCenter = temp[1]
                    #distance = math.sqrt((math.pow(xCenter,2)-math.pow(320,2))+(math.pow(yCenter,2)-0))
                    distance = math.sqrt(math.pow(xCenter-480, 2)+math.pow(yCenter-0,2))
                    cv2.putText(frame, str(distance) , (25,25),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
                    #D = np.linalg.norm(cx-cy)
                    #print(D)
        """
        x,y,w,h = cv2.boundingRect(img)            
        cv2.rectangle(mask,(x,y),(x+w,y+h),(0,255,0),2)
        plt.imshow(frame)
        print("Distances: vertical: %d, horizontal: %d" % (h,w))
        """
            
            #a = cv2.magnitude(centers[0],centers[1], 2)
            #print(a)

        
    imgStack = stck.stackImages(0.5,([frame,thresh,maskerode,maskerode],[maskrange,frame,frame,frame],[maskerode,maskdilation,maskopen,maskclose]))
    #imgStack = stck.stackImages(0.9,([frame,maskerode,maskdilation],[maskopen,maskclose,frame]))
    cv2.imshow("Stacked", imgStack)


    key = cv2.waitKey(1)
    if key == 27: #esc
        break