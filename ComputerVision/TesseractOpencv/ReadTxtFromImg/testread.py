import pytesseract
import cv2

frame = cv2.imread("txt.png")
text = pytesseract.image_to_string(frame)
boxes = pytesseract.image_to_boxes(frame)
#print(text)
print(boxes)