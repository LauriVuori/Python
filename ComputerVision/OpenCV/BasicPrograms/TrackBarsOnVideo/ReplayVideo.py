import cv2 as cv
import numpy as np

def Frames(frame_nr):
    global vid
    video.set(cv.CAP_PROP_POS_FRAMES, frame_nr)

def setSpeed(value):
    global PlaySpeed
    PlaySpeed = max(value,1)


video = cv2.VideoCapture("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\TrackBarsOnVideo\\test.mp4")

nr_of_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))


cv2.namedWindow("Player")

playSpeed = 50

cv2.createTrackbar("Frame", "Player", 0,nr_of_frames,Frames)
cv2.createTrackbar("Speed", "Player", playSpeed,100,setSpeed)

while True:
  
    ret, frame = video.read()
    if ret:
        cv2.imshow("Player", frame)

        cv2.setTrackbarPos("Frame","Player", int(video.get(cv2.CAP_PROP_POS_FRAMES)))
    else:
        break

    key = cv2.waitKey(playSpeed)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()