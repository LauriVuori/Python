import matplotlib.pyplot as plt
import cv2
import numpy as np
import Func

image = Func.create_canvas_matplotlib(400,400)

image = cv2.line(image, (0,0), (400,400), (255,0,0), 2)
image = cv2.rectangle(image, (0,0), (200,200), (0,255,0), 2)
ret, p1, p2 = cv2.clipLine((0, 0, 200, 200), (0, 0), (400, 400))
if ret:
    cv2.line(image, p1, p2, (0,255,255), 3)

Func.show_with_matplotlib(image, "test")

