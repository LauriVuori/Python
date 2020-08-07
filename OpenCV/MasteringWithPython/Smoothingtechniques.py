import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func


Func.create_canvas_matplotlib(500,500)
image = cv2.imread('keyboard.jpg')

kernel_averaging_10_10 = np.ones((10, 10), np.float32) / 100
kernel_averaging_5_5 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04]])
smooth_image_f2D_5_5 = cv2.filter2D(image, -1, kernel_averaging_5_5)
smooth_image_f2D_10_10 = cv2.filter2D(image, -1, kernel_averaging_10_10)
smooth_image_b = cv2.blur(image, (10, 10))
smooth_image_bfi = cv2.boxFilter(image, -1, (10, 10), normalize=True)
smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)
smooth_image_mb = cv2.medianBlur(image, 9)

while True:
    smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)

    image_stack = Func.stackImages(0.2,([smooth_image_bf,smooth_image_f2D_5_5,smooth_image_gb],[smooth_image_gbsmooth_image_mb]))
    cv2.imshow("Stack",image_stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break