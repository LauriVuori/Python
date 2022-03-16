import cv2
from cv2 import compare
import numpy as np
import Func

def empty(x):
    pass

font = cv2.FONT_HERSHEY_COMPLEX

cv2.namedWindow("TrackBars", cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow("TrackBars", 640, 500)

cv2.createTrackbar("Hue min", "TrackBars", 120, 255, empty)
cv2.createTrackbar("Hue max", "TrackBars", 154, 255, empty)

cv2.createTrackbar("Sat min", "TrackBars", 217, 255, empty)
cv2.createTrackbar("Sat max", "TrackBars", 255, 255, empty)

cv2.createTrackbar("Val min", "TrackBars", 106, 255, empty)
cv2.createTrackbar("Val max", "TrackBars", 212, 255, empty)

cv2.createTrackbar("min_area", "TrackBars", 2400, 10000, empty)
cv2.createTrackbar("max_area", "TrackBars", 6000, 10000, empty)

cap = cv2.VideoCapture(0)

def ret_red_mask(original, imgHSV):
    h_min = 0
    h_max = 36
    s_min = 28
    s_max = 255
    v_min = 72
    v_max = 255

    red_lower = np.array([h_min, s_min, v_min], np.uint8)
    red_upper = np.array([h_max, s_max, v_max], np.uint8)
    r_mask = cv2.inRange(imgHSV, red_lower, red_upper)
    kernel = np.ones((5, 5), "uint8")
    red_mask = cv2.dilate(r_mask, kernel)
    imgResult = cv2.bitwise_and(original, original, mask=r_mask)
    return imgResult, red_mask


def ret_blue_mask(original, imgHSV):
    h_min = 120
    h_max = 154
    s_min = 217
    s_max = 255
    v_min = 27
    v_max = 212
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")

    blue_lower = np.array([h_min, s_min, v_min], np.uint8)
    blue_upper = np.array([h_max, s_max, v_max], np.uint8)
    b_mask = cv2.inRange(imgHSV, blue_lower, blue_upper)
    kernel = np.ones((5, 5), "uint8")
    blue_mask = cv2.dilate(b_mask, kernel)
    imgResult = cv2.bitwise_and(original, original, mask=b_mask)
    return imgResult, blue_mask

def ret_green_mask(original, imgHSV):
    h_min = 53
    h_max = 67
    s_min = 36
    s_max = 255
    v_min = 41
    v_max = 255
    # h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    # h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    # s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    # s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    # v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    # v_max = cv2.getTrackbarPos("Val max", "TrackBars")
    green_lower = np.array([h_min, s_min, v_min], np.uint8)
    green_upper = np.array([h_max, s_max, v_max], np.uint8)
    g_mask = cv2.inRange(imgHSV, green_lower, green_upper)
    kernel = np.ones((5, 5), "uint8")
    green_mask = cv2.dilate(g_mask, kernel)
    imgResult = cv2.bitwise_and(original, original, mask=green_mask)
    return imgResult, green_mask

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", 1000, 600)
rectangle_line_size = 3
text_size = 5

rgb_leds = [0]*3
last_rgb_leds = [0]*3
counter = 0
RED = 0
GREEN = 1
BLUE = 2
rgb_leds[RED] = 0
rgb_leds[GREEN] = 0
rgb_leds[BLUE] = 0
while True:
    start = cv2.getTickCount()

    _, frame = cap.read()
    imageFrame = frame

    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_result, r_mask = ret_red_mask(frame, imgHSV)
    blue_result, b_mask = ret_blue_mask(frame, imgHSV)
    green_result, g_mask = ret_green_mask(frame, imgHSV)

    # green_lower = np.array([h_min, s_min, v_min], np.uint8)
    # green_upper = np.array([h_max, s_max, v_max], np.uint8)
    # gree_mask = cv2.inRange(imgHSV, green_lower, green_upper)
    # kernel = np.ones((5, 5), "uint8")
    # green_mask = cv2.dilate(gree_mask, kernel)
    # green_result = cv2.bitwise_and(frame, frame, mask=gree_mask)
    contours, hierarchy = cv2.findContours(r_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    

    min_area = cv2.getTrackbarPos("min_area", "TrackBars")
    max_area = cv2.getTrackbarPos("max_area", "TrackBars")
    rgb_leds[RED] = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if ((area > min_area) and (area < max_area)):
            # rect = cv2.minAreaRect(contour)
            # box = cv2.boxPoints(rect)
            # box = np.int0(box)
            # boxarea = cv2.contourArea(box)
            rgb_leds[RED] = 1
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), rectangle_line_size)
              
            cv2.putText(imageFrame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 5.0,
                        (0, 0, 255), text_size) 

        

    
    contours, hierarchy = cv2.findContours(b_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    rgb_leds[BLUE] = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if ((area > min_area) and (area < max_area)):
            rgb_leds[BLUE] = 1
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 0, 0), rectangle_line_size)
              
            cv2.putText(imageFrame, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 5.0,
                        (255, 0, 0), text_size)
            


    contours, hierarchy = cv2.findContours(g_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    rgb_leds[GREEN] = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if ((area > min_area) and (area < max_area)):
            rgb_leds[GREEN] = 1
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 255, 0), rectangle_line_size)
              
            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 5.0,
                        (0, 255, 0), text_size) 
            


    stop = cv2.getTickCount()
    time = (stop - start)/ cv2.getTickFrequency()
    cv2.putText(frame, str(rgb_leds), (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 3)
    cv2.putText(frame, str(1/time), (150, 300), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 3)
    cv2.putText(green_result, "Green result", (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 5, (209, 80, 0, 255), 3)
    cv2.putText(blue_result, "Blue result", (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 5, (209, 80, 0, 255), 3)
    cv2.putText(red_result, "Red result", (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 5, (209, 80, 0, 255), 3)
    
    Imgstack = Func.stackImages(0.2, ([frame, imgHSV], [g_mask, green_result], [b_mask, blue_result], [r_mask, red_result]))
    cv2.imshow("Frame", Imgstack)
    cv2.imshow("Original", frame)

    # if (rgb_leds[i] != last_rgb_leds[i]):
    if (sum(rgb_leds) != sum(last_rgb_leds)):
        counter = counter + 1
        if (counter > 6):
            last_rgb_leds = rgb_leds.copy()
            counter = 0
            print("UPDATE" + str(last_rgb_leds))
    # print(str(rgb_leds) + str(last_rgb_leds))
    # print(counter)
    key = cv2.waitKey(1)
    if key == 27:  # esc
        cap.release()
        cv2.destroyAllWindows()
        break
