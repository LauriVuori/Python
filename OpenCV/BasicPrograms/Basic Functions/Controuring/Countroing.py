import cv2 as cv
import imutils

image = cv.imread("blop.png") 
window_name = 'image'

image = cv.imread("blop.png")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5, 5), 0)
# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv.threshold(gray, 45, 255, cv.THRESH_BINARY)[1]
thresh = cv.erode(thresh, None, iterations=2)
thresh = cv.dilate(thresh, None, iterations=2)
# find contours in thresholded image, then grab the largest
# one
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
	cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv.contourArea)

cv.imshow(window_name, image)
cv.waitKey(0)   
cv.destroyAllWindows()