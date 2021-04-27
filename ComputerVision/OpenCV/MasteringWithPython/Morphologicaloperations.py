import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func

# This function creates the specific kernel to be used when performing the morphological operations
def build_kernel(kernel_type, kernel_size):
    """Creates the specific kernel: MORPH_ELLIPSE, MORPH_CROSS or MORPH_RECT"""

    if kernel_type == cv2.MORPH_ELLIPSE:
        # We build a elliptical kernel
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    elif kernel_type == cv2.MORPH_CROSS:
        # We build a cross-shape kernel
        return cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)
    else:  # cv2.MORPH_RECT
        # We build a rectangular kernel:
        return cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

# This function erodes the image
def erode(image, kernel_type, kernel_size):
    """Erodes the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    erosion = cv2.erode(image, kernel, iterations=1)
    return erosion


# This function dilates the image
def dilate(image, kernel_type, kernel_size):
    """Dilates the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    dilation = cv2.dilate(image, kernel, iterations=1)
    return dilation


# This function closes the image
# Closing = dilation + erosion
def closing(image, kernel_type, kernel_size):
    """Closes the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    clos = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return clos


# This function opens the image
# Opening = erosion + dilation
def opening(image, kernel_type, kernel_size):
    """Opens the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    ope = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return ope


# This function applies the morphological gradient to the image
def morphological_gradient(image, kernel_type, kernel_size):
    """Applies the morfological gradient to the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    morph_gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    return morph_gradient


# This function closes and opens the image
def closing_and_opening(image, kernel_type, kernel_size):
    """Closes and opens the image with the specified kernel type and size"""

    closing_img = closing(image, kernel_type, kernel_size)
    opening_img = opening(closing_img, kernel_type, kernel_size)
    return opening_img


# This function opens and closes the image
def opening_and_closing(image, kernel_type, kernel_size):
    """Open and closes the image with the specified kernel type and size"""

    opening_img = opening(image, kernel_type, kernel_size)
    closing_img = closing(opening_img, kernel_type, kernel_size)
    return closing_img


# Implemented morphological operations to be used
# The key identifies the morphological operation to be used
# The value is the function to be called when the corresponding key is used
morphological_operations = {
    'erode': erode,
    'dilate': dilate,
    'closing': closing,
    'opening': opening,
    'gradient': morphological_gradient,
    'closing|opening': closing_and_opening,
    'opening|closing': opening_and_closing
}
def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)

def apply_morphological_operation(array_img, morphological_operation, kernel_type, kernel_size):
    """Applies the defined morphological operations to the array of images with the specified kernel type and size"""

    morphological_operation_result = []
    for index_image, image in enumerate(array_img):
        result = morphological_operations[morphological_operation](image, kernel_type, kernel_size)
        morphological_operation_result.append(result)
    return morphological_operation_result

kernel_size_3_3 = (3, 3)
kernel_size_5_5 = (5, 5)

image = cv2.imread('keyboard.jpg')
smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
sharpen_image = unsharped_filter(smooth_image_bf)
gray_image = cv2.cvtColor(sharpen_image, cv2.COLOR_BGR2GRAY)
ret, thresh_image = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY_INV)
image_erode1 = erode(thresh_image, cv2.MORPH_ELLIPSE, kernel_size_3_3)
image_erode2 = erode(thresh_image, cv2.MORPH_CROSS, kernel_size_3_3)
image_erode3 = erode(thresh_image, cv2.MORPH_RECT, kernel_size_3_3)

image_dilate1 = dilate(thresh_image, cv2.MORPH_ELLIPSE, kernel_size_3_3)
image_dilate2 = dilate(thresh_image, cv2.MORPH_CROSS, kernel_size_3_3)
image_dilate3 = dilate(thresh_image, cv2.MORPH_RECT, kernel_size_3_3)

image_dilero1 = dilate(image_erode1 , cv2.MORPH_ELLIPSE, kernel_size_3_3)
image_dilero2 = dilate(image_erode2, cv2.MORPH_CROSS, kernel_size_3_3)
image_dilero3 = dilate(image_erode3, cv2.MORPH_RECT, kernel_size_3_3)







while True:

    image_stack = Func.stackImages(0.17,([image_erode1,image_erode2,image_erode3],[image_dilate1,image_dilate2,image_dilate3],[image_dilero1,image_dilero2,image_dilero3]))
    cv2.imshow("Stack",image_stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break