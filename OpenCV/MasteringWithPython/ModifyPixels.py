import cv2
import numpy as np
img = cv2.imread('txt.png', cv2.IMREAD_GRAYSCALE)
# intensity
img[0:50,0:50] = 0
while True:
    cv2.imshow("frame", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        exit()