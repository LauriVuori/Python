"""
Useful functions to use computer vision\n
show_with_matplotlib(img, title)\n
create_canvas_matplotlib(x,y):\n
colors['red']\n
def stackImages(scale,imgArray):\n
def resize_frame(frame,percent):\n
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np

def show_with_matplotlib(img, title):
    """
    show image using matplotlib
    """
    img_rgb = img[:, :, ::-1]
    plt.imshow(img_rgb)
    plt.title(title)
    plt.show()

def create_canvas_matplotlib(x,y):
    """
    create canvas and give x y values
    """
    image = np.zeros((y, x, 3), dtype="uint8")
    image[:] = (220, 220, 220)
    return image

colors = {
        'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
        'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
        'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
        'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)
        }

def resize_frame(frame,percent):
    """
    resize frame, (frame, percent)
    """
    scale_percent = percent
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    return resized

def stackImages(scale,imgArray):
    """
    Stack images example: imgStack = Func.stackImages(0.6,([frame,gray,thresh],[img,test,copy]))
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def put_description(frame, text):
    """
    not working
    Put description on window
    """
    cv2.putText(frame, text , (100,100), cv2.FONT_HERSHEY_COMPLEX, 14, (0,0,255)) 
    return frame

def unsharped_filter(img):
    """The unsharp filter enhances edges subtracting the smoothed image from the original image"""

    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    return cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)

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

def closing(image, kernel_type, kernel_size):
    """Closes the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    clos = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return clos

# This function applies the morphological gradient to the image
def morphological_gradient(image, kernel_type, kernel_size):
    """Applies the morfological gradient to the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    morph_gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    return morph_gradient

def opening(image, kernel_type, kernel_size):
    """Opens the image with the specified kernel type and size"""

    kernel = build_kernel(kernel_type, kernel_size)
    ope = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return ope

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

def build_kernel(kernel_type, kernel_size):
    """Creates the specific kernel: MORPH_ELLIPSE, MORPH_CROSS or MORPH_RECT"""
    if kernel_type == cv2.MORPH_ELLIPSE:
        # We build a elliptical kernel
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    elif kernel_type == cv2.MORPH_CROSS:
        # We build a cross-shape kernel
        return cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)
    elif kernel_type == cv2.MORPH_RECT:
        # We build a rectangular kernel:
        return cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    
def morptransof(frame):
    kernel_size_3_3 = (3, 3)
    kernel_size_5_5 = (5, 5)
    kernel_types = [cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS, cv2.MORPH_RECT]
    erode = Func.erode(frame, kernel_types[0], kernel_size_3_3)
    dilate = Func.dilate(erode, kernel_types[0], kernel_size_3_3)
    closing = Func.closing(dilate, kernel_types[0], kernel_size_3_3)
    opening = Func.opening(closing, kernel_types[0], kernel_size_3_3)
    gradient = Func.morphological_gradient(opening, kernel_types[0], kernel_size_3_3)
    closeopen = Func.closing_and_opening(gradient,kernel_types[0], kernel_size_3_3)
    openclose = Func.opening_and_closing(closeopen, kernel_types[0], kernel_size_3_3)
    return openclose