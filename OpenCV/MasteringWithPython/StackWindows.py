import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('logo.jpg')


#split channels into its three channels
#Split is slow, use numpy
#b, g, r = cv2.split(img)
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
img_matplotlib = cv2.merge([b, r, g])
img2 = img[:, :, ::-1]
img_stack = np.concatenate((img, img_matplotlib,img2), axis=1)
cv2.imshow("Stack",img_stack)
cv2.waitKey(0)
cv2.destroyAllWindows()