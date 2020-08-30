import cv2
import numpy as np
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

# mouse callback function
def interactive_drawing(event,x,y,flags,param):
    global ix,iy,drawing, mode

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
                ix=x
                iy=y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
    return x,y


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

# every move calls function draw_circle, 
cv2.setMouseCallback('image', interactive_drawing)



while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(mouseX,mouseY)