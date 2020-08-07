import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func


def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)


image = cv2.imread('keyboard.jpg')

kernel_sharpen_1 = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

kernel_sharpen_2 = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

kernel_sharpen_3 = np.array([[1, 1, 1],
                             [1, -7, 1],
                             [1, 1, 1]])

kernel_sharpen_4 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0

# Apply all the kernels we have created:
sharp_image_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
sharp_image_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
sharp_image_3 = cv2.filter2D(image, -1, kernel_sharpen_3)
sharp_image_4 = cv2.filter2D(image, -1, kernel_sharpen_4)

# Try the unsharped filter:
sharp_image_5 = unsharped_filter(image)

while True:
    smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)

    image_stack = Func.stackImages(0.2,([image,sharp_image_4,sharp_image_5]))
    cv2.imshow("Stack",image_stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break