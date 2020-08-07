#img = cv.imread("C:\\Users\\teija\\OneDrive\\Git\\Python\\OpenCV\\ResizingCropping\\edge.png")
import cv2 as cv
import numpy as np
#512,512, 3 channel
img = np.zeros((512,512,3),np.uint8)
#512,512
print(img.shape)

#blue, :<- full image , example 300:500, 350:450
img[:]=255,0,0
#start, end, color, thickness
cv.line(img, (0,0),(300,300), (0,255,255), 3)
#cv.line(img, (0,0), (img.shape[1],img.shape[0]),(0,255,255),3)
#thickness->cv.FILLED
cv.rectangle(img,(0,0),(250,350),(0,255,0),3)

cv.circle(img,(400,50),30,(255,255,0),5)

cv.putText(img, "OPENCV TEST", (120,100), cv.FONT_ITALIC, 1, (0,150,0), 1)


cv.imshow("black",img)

cv.waitKey(0)