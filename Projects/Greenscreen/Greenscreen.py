import cv2
import Func
import numpy as np
import timeit

def empty(x):
    pass
def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)
def Trackbars():
    cv2.namedWindow("Face1")
    cv2.resizeWindow("Face1", 600,600)
    cv2.createTrackbar("Hue min", "Face1", 0, 179, empty)
    cv2.createTrackbar("Hue max", "Face1", 179, 179, empty)

    cv2.createTrackbar("Sat min", "Face1", 0, 255, empty)
    cv2.createTrackbar("Sat max", "Face1", 50, 255, empty)

    cv2.createTrackbar("Val min", "Face1", 0, 255, empty)
    cv2.createTrackbar("Val max", "Face1", 255, 255, empty)

    cv2.namedWindow("Face2")
    cv2.resizeWindow("Face2", 600,600)
    cv2.createTrackbar("Hue min", "Face2", 0, 179, empty)
    cv2.createTrackbar("Hue max", "Face2", 179, 179, empty)

    cv2.createTrackbar("Sat min", "Face2", 56, 255, empty)
    cv2.createTrackbar("Sat max", "Face2", 255, 255, empty)

    cv2.createTrackbar("Val min", "Face2", 66, 255, empty)
    cv2.createTrackbar("Val max", "Face2", 255, 255, empty)

    cv2.namedWindow("Face3")
    cv2.resizeWindow("Face3", 600,600)
    cv2.createTrackbar("Hue min", "Face3", 0, 179, empty)
    cv2.createTrackbar("Hue max", "Face3", 179, 179, empty)

    cv2.createTrackbar("Sat min", "Face3", 74, 255, empty)
    cv2.createTrackbar("Sat max", "Face3", 255, 255, empty)

    cv2.createTrackbar("Val min", "Face3", 0, 255, empty)
    cv2.createTrackbar("Val max", "Face3", 85, 255, empty)


def FrameMasking(image, Face1_lower, Face1_upper, Face2_lower, Face2_upper, Face3_lower, Face3_upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    filtered = cv2.bilateralFilter(hsv, 5, 10, 10)
    sharpened = unsharped_filter(filtered)
    mask_Face1 = cv2.inRange(sharpened, Face1_lower, Face1_upper)
    mask_Face2 = cv2.inRange(sharpened, Face2_lower, Face2_upper)
    mask_Face3 = cv2.inRange(sharpened, Face3_lower, Face3_upper)

    mask_Face1 = Func.erode(mask_Face1, cv2.MORPH_ELLIPSE, (3,3))
    mask_Face1 = Func.dilate(mask_Face1, cv2.MORPH_ELLIPSE, (3,3))
    mask_Face2 = Func.erode(mask_Face2, cv2.MORPH_ELLIPSE, (3,3))
    mask_Face2 = Func.dilate(mask_Face2, cv2.MORPH_ELLIPSE, (3,3))
    mask_Face3 = Func.erode(mask_Face3, cv2.MORPH_ELLIPSE, (3,3))
    mask_Face3 = Func.dilate(mask_Face3, cv2.MORPH_ELLIPSE, (3,3))
    #mask_face1 = cv2.bitwise_not(mask_Face1)
    #frame = mask_Face2 + mask_Face1 
    frame = cv2.bitwise_and(mask_Face3,mask_Face2, mask = mask_Face1)
    return mask_Face1, mask_Face2, mask_Face3, frame


def Trackbarpositions():
    Face1_h_min = cv2.getTrackbarPos("Hue min", "Face1")
    Face1_h_max = cv2.getTrackbarPos("Hue max", "Face1")

    Face1_s_min = cv2.getTrackbarPos("Sat min", "Face1")
    Face1_s_max = cv2.getTrackbarPos("Sat max", "Face1")

    Face1_v_min = cv2.getTrackbarPos("Val min", "Face1")
    Face1_v_max = cv2.getTrackbarPos("Val max", "Face1")

    Face2_h_min = cv2.getTrackbarPos("Hue min", "Face2")
    Face2_h_max = cv2.getTrackbarPos("Hue max", "Face2")

    Face2_s_min = cv2.getTrackbarPos("Sat min", "Face2")
    Face2_s_max = cv2.getTrackbarPos("Sat max", "Face2")

    Face2_v_min = cv2.getTrackbarPos("Val min", "Face2")
    Face2_v_max = cv2.getTrackbarPos("Val max", "Face2")

    Face3_h_min = cv2.getTrackbarPos("Hue min", "Face3")
    Face3_h_max = cv2.getTrackbarPos("Hue max", "Face3")

    Face3_s_min = cv2.getTrackbarPos("Sat min", "Face3")
    Face3_s_max = cv2.getTrackbarPos("Sat max", "Face3")

    Face3_v_min = cv2.getTrackbarPos("Val min", "Face3")
    Face3_v_max = cv2.getTrackbarPos("Val max", "Face3")
    """
    c_h_min = cv2.getTrackbarPos("Hue min", "Face1")
    c_h_max = cv2.getTrackbarPos("Hue max", "Face1")

    c_s_min = cv2.getTrackbarPos("Sat min", "Cupcolor")
    c_s_max = cv2.getTrackbarPos("Sat max", "Cupcolor")

    c_v_min = cv2.getTrackbarPos("Val min", "Cupcolor")
    c_v_max = cv2.getTrackbarPos("Val max", "Cupcolor")
    """
    Face1_lower = np.array([Face1_h_min, Face1_s_min, Face1_v_min])
    Face1_upper = np.array([Face1_h_max, Face1_s_max, Face1_v_max])

    Face2_lower = np.array([Face2_h_min, Face2_s_min, Face2_v_min])
    Face2_upper = np.array([Face2_h_max, Face2_s_max, Face2_v_max])

    Face3_lower = np.array([Face3_h_min, Face3_s_min, Face3_v_min])
    Face3_upper = np.array([Face3_h_max, Face3_s_max, Face3_v_max])

    return Face1_lower, Face1_upper, Face2_lower, Face2_upper, Face3_lower, Face3_upper


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1088)
_, frame = cap.read()
FrameHeight, FrameWidth, _ = frame.shape
print("Height: ", FrameHeight, "Width:", FrameWidth)
TimeCounter = 0
TimerAverage = 0
TimerSum = 0
Trackbars()
while True:
    starttime = timeit.default_timer()
    _, frame = cap.read()
    Face1_lower, Face1_upper, Face2_lower, Face2_upper, Face3_lower, Face3_upper= Trackbarpositions()
    mask1, mask2, mask3, frame= FrameMasking(frame, Face1_lower, Face1_upper, Face2_lower, Face2_upper, Face3_lower, Face3_upper)
    Imgstack = Func.stackImages(0.3,([mask1,mask2,mask3],[frame,mask2,frame]))
    cv2.imshow("pic", Imgstack)
    TimerSum += timeit.default_timer() - starttime
    TimeCounter += 1
    key = cv2.waitKey(1)
    if key == 27:
        print("Average execution time is:", 1/(TimerSum / TimeCounter), "fps")
        print("break")
        exit()
