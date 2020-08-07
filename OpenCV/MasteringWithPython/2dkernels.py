import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func


def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)


image = cv2.imread('keyboard.jpg')
#smoot
image = cv2.bilateralFilter(image, 5, 10, 10)
#sharpen
image = unsharped_filter(image)
# We try different kernels
# Identify kernel (does not modify the image)
kernel_identity = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]])

# Try different kernels for edge detection:
kernel_edge_detection_1 = np.array([[1, 0, -1],
                                    [0, 0, 0],
                                    [-1, 0, 1]])

kernel_edge_detection_2 = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

kernel_edge_detection_3 = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])

# Try different kernels for sharpening:
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

kernel_unsharp_masking = -1 / 256 * np.array([[1, 4, 6, 4, 1],
                                              [4, 16, 24, 16, 4],
                                              [6, 24, -476, 24, 6],
                                              [4, 16, 24, 16, 4],
                                              [1, 4, 6, 4, 1]])

# Try different kernels for smoothing:
kernel_blur = 1 / 9 * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])

gaussian_blur = 1 / 16 * np.array([[1, 2, 1],
                                   [2, 4, 2],
                                   [1, 2, 1]])

# Try a kernel for embossing:
kernel_emboss = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]])

# Try different kernels for edge detection:
sobel_x_kernel = np.array([[1, 0, -1],
                           [2, 0, -2],
                           [1, 0, -1]])

sobel_y_kernel = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

outline_kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])

# Apply all the kernels:
original_image = cv2.filter2D(image, -1, kernel_identity)
edge_image_1 = cv2.filter2D(image, -1, kernel_edge_detection_1)
edge_image_2 = cv2.filter2D(image, -1, kernel_edge_detection_2)
edge_image_3 = cv2.filter2D(image, -1, kernel_edge_detection_3)
sharpen_image = cv2.filter2D(image, -1, kernel_sharpen)
unsharp_masking_image = cv2.filter2D(image, -1, kernel_unsharp_masking)
blur_image = cv2.filter2D(image, -1, kernel_blur)
gaussian_blur_image = cv2.filter2D(image, -1, gaussian_blur)
emboss_image = cv2.filter2D(image, -1, kernel_emboss)
sobel_x_image = cv2.filter2D(image, -1, sobel_x_kernel)
sobel_y_image = cv2.filter2D(image, -1, sobel_y_kernel)
outline_image = cv2.filter2D(image, -1, outline_kernel)

while True:


    image_stack = Func.stackImages(0.1,([edge_image_1,edge_image_2,edge_image_3]))
    cv2.imshow("Stack",image_stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break