import cv2
import stackmodule as stack
import pytesseract
def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600,600)
cv2.createTrackbar("Gray min", "Trackbars", 43, 255, nothing)
cv2.createTrackbar("Gray max", "Trackbars", 255, 255, nothing)


frame = cv2.imread("txt.png")
cv2.namedWindow("Stacked", cv2.WINDOW_NORMAL) 

while True:
    g_min = cv2.getTrackbarPos("Gray min", "Trackbars")
    g_max = cv2.getTrackbarPos("Gray max", "Trackbars")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, thresh = cv2.threshold(blurred, g_min, g_max, cv2.THRESH_BINARY)
    hFrame, wFrame, _ = frame.shape
    #['m', '221', '282', '237', '293', '0'], ['text','x','y','width','height']
    #boxes = pytesseract.image_to_boxes(frame)
    boxes = pytesseract.image_to_data(frame)
    #print(boxes)
    #print(boxes)

    for b in boxes.splitlines():
        b = b.split(' ')
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(frame,(x,hFrame-y),(w,hFrame-h),(0,0,255),1)
        cv2.putText(frame, b[0], (x, hFrame-y+125), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,255),1)
        
    imgStack = stack.stackImages(1,([frame,frame],[thresh,thresh]))
    while True:
        cv2.imshow("Stacked", imgStack)
        key = cv2.waitKey(1)
        if key == 27: #esc
            exit()
        