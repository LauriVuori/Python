import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('logo.jpg')
#split channels into its three channels
#Split is slow, use numpy
#b, g, r = cv2.split(img)
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
img_matplotlib = cv2.merge([r, g, b])

img2 = img[:, :, ::-1]
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()

