import cv2
import numpy as np
from PIL import ImageGrab
#     events
#     EVENT_MOUSEMOVE     = 0,
#     EVENT_LBUTTONDOWN   = 1,
#     EVENT_RBUTTONDOWN   = 2,
#     EVENT_MBUTTONDOWN   = 3,
#     EVENT_LBUTTONUP     = 4,
#     EVENT_RBUTTONUP     = 5,
#     EVENT_MBUTTONUP     = 6,
#     EVENT_LBUTTONDBLCLK = 7,
#     EVENT_RBUTTONDBLCLK = 8,
#     EVENT_MBUTTONDBLCLK = 9,
#     EVENT_MOUSEWHEEL    = 10,
#     EVENT_MOUSEHWHEEL   = 11,

drawing=False # true if mouse is pressed
mode=True # if True, draw rectangle. Press 'm' to toggle to curve
# img = np.zeros((512,512,3), np.uint8)

# WhiteImg = np.zeros([512,512,1],dtype=np.uint8)
# WhiteImg.fill(255)

# img = WhiteImg
xList = []
yList = []

def test():    
    global img, xList, yList 
    cv2.namedWindow('image')
    STOP = 0
    while(STOP == 0):
        img = ImageGrab.grab(bbox=(0,0,1980,1240))
        img = np.uint8(img)

        
        # every move calls function draw_circle, 
        cv2.setMouseCallback('image', rectangle_drawing)
        if len(xList) == 2:
            img = cv2.rectangle(img, (xList[0],yList[0]), (xList[1],xList[1]), (0,0,255))
            xList = []
            yList = []


        cv2.imshow('image',img)

        k = cv2.waitKey(1)
        if k == 27:
            cv2.destroyWindow('image')
            STOP = 1
        elif k == ord('a'):
            print(mouseX, mouseY)


# mouse callback function
def interactive_drawing(event, x, y,flags, param):
    global ix, iy, drawing, mode, img, xList, yList

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                img = cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
                ix=x
                iy=y
                xList.append(x)
                yList.append(y)

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            img = cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
            xList.append(x)
            yList.append(y)

def rectangle_drawing(event, x, y,flags, param):
    global ix, iy, drawing, mode, img, xList, yList

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
        xList.append(ix)
        yList.append(iy)


    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                img = cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
                ix=x
                iy=y

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            img = cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
            xList.append(x)
            yList.append(y)
def Drawlist(Dots):
    pass

test()