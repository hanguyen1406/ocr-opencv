import cv2
import numpy as np

# Load the image
image = cv2.imread('./img.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold to get binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Morphological operations to clean up the text
kernel = np.ones((1, 1), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Find contours to identify small white dots
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) < 50:  # Adjust the area threshold as needed
        cv2.drawContours(binary, [contour], -1, 0, -1)  # Remove small white dots by filling them with black

# Paint the background black
result = cv2.bitwise_and(image, image, mask=binary)
result[binary == 0] = (0, 0, 0)  # Set the background to black

# Save and display the result
cv2.imwrite('cleaned_text.png', result)
cv2.imshow('Cleaned Text', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
