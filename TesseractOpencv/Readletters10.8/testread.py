import pytesseract
import cv2
import numpy as np

# frame = cv2.imread("kboard.jpg")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)

while True:
    _, frame = cap.read()
    text = pytesseract.image_to_string(frame)
    boxes = pytesseract.image_to_boxes(frame)
    print(boxes)
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    hFrame, wFrame, _ = frame.shape
    for b in boxes.splitlines():
            b = b.split(' ')
            
            x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(frame,(x,hFrame-y),(w,hFrame-h),(0,0,255),5)
            # cv2.putText(frame, b[0], (x, hFrame-y+125), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,255),1)
    cv2.imshow("img", frame)
    key = cv2.waitKey(1)
    if key == 27: #esc
        exit()