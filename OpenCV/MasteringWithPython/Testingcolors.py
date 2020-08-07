import constant
import numpy as np
import matplotlib.pyplot as plt
import cv2

def show_with_matplotlib(img, title):
    img_rgb = img[:, :, ::-1]
    plt.imshow(img_rgb)
    plt.title(title)
    plt.show()

print("yellow: '{}'".format(constant.YELLOW))

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red:': (0,0,255), 'rand': np.random.randint(0, high=256, size=(3,)).tolist()}

print("Random:", colors['rand'])

image = np.zeros((500,500, 3), dtype="uint8")
#background
image[:] = colors['rand']

separation = 40
for key in colors:
    cv2.line(image, (0, separation), (500, separation), colors[key], 10)
    separation += 40
show_with_matplotlib(image, "Colors")