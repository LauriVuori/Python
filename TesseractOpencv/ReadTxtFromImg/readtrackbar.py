import pytesseract
import cv2
def nothing(x):
    pass
cv2.namedWindow("T")
cv2.resizeWindow("T", 600,600)
cv2.createTrackbar("pic", "T", 4, 100, nothing)
cv2.createTrackbar("scale", "T", 100, 1000, nothing)
cv2.createTrackbar("Gray min", "T", 87, 255, nothing)
cv2.createTrackbar("Gray max", "T", 255, 255, nothing)
while True:
    i = cv2.getTrackbarPos("pic","T")
    scale = cv2.getTrackbarPos("scale","T")
    gmin = cv2.getTrackbarPos("Gray min","T")
    gmax = cv2.getTrackbarPos("Gray max", "T")
    frame = cv2.imread("./keys/key"+str(i)+".png")
    # frame = cv2.cvtColor(frame,)
    scale_percent = scale
    width = int(frame.shape[1]*scale_percent /100)
    height = int(frame.shape[0]*scale_percent /100)
    dsize = (width, height)
    frame = cv2.resize(frame, dsize)
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, gmin, gmax, cv2.THRESH_BINARY_INV)
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(thresh, [cnt], 0, [0,0,0], 3)
    text = pytesseract.image_to_string(thresh)
    print(text)
    boxes = pytesseract.image_to_boxes(thresh)
    hFrame, wFrame, _ = frame.shape
    for b in boxes.splitlines():
            b = b.split(' ')
            x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(frame,(x,hFrame-y),(w,hFrame-h),(0,0,255),1)
            cv2.putText(frame, b[0], (x, hFrame-y+125), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,255),1)

    cv2.imshow("Stacked", thresh)
    key = cv2.waitKey(1) 
    if key == 27: #esc
        exit()