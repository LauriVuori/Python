import cv2 as cv

capture = cv.VideoCapture(0)

#id 3, width
capture.set(3,640)
#id 4, height
capture.set(4,480)
#id 10, brightness


while True:
    success, img = capture.read()
    #Show window
    cv.imshow("Video", img)
    #wait and escape on key q
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break