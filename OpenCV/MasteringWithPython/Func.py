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
