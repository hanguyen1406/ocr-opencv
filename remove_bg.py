import cv2
import numpy as np

image = cv2.imread('./img.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((1, 1), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imwrite('cleaned_text.png', binary)
cv2.imshow('Cleaned Text', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
