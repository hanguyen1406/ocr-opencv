import cv2

img = cv2.imread('./img.jpg', 0)
edges = cv2.Canny(img, 100, 200)
cv2.imwrite('./cleaned_text.png', edges)