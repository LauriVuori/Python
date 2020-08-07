import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: EVENT_LBUTTONDBLCLK")
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x,y), 10, Func.colors['rand'], -1)
        print("event: EVENT_LBUTTONDOWN")

cv2.namedWindow("Image mouse")
cv2.setMouseCallback("Image mouse", draw_circle)
image = Func.create_canvas_matplotlib(400,400)
while True:
    cv2.imshow("Image mouse", image)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()