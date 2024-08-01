import cv2
import numpy as np

image = cv2.imread('./img.jpg')


h, w = image.shape[:2]
imgScale = cv2.resize(image, (int(w*2), int(h*2)), interpolation = cv2.INTER_LINEAR)


cv2.imwrite('./img.jpg', imgScale)