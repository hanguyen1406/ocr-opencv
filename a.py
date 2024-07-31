import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

image = cv2.imread('img.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

n_boxes = len(d['text'])

for i in range(n_boxes):
    if int(d['conf'][i]) > 0:  # Check if the word is recognized with some confidence
        x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
        word_image = gray[y:y+h, x:x+w]
        
        word_image_pil = Image.fromarray(word_image)
        word_image_pil.save(f'word_{i}.jpg')

print("Words have been extracted and saved as separate images.")


