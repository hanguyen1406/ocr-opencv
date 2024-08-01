import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

image = cv2.imread('./cleaned_text.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
config = '--psm 6 -l vie'
d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

n_boxes = len(d['text'])

text_center = []

for i in range(n_boxes):
    if int(d['conf'][i]) > 0:  # Check if the word is recognized with some confidence
        x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
        x -= 10
        y -= 12
        w += 15
        h += 16
        word_image = gray[y:y+h, x:x+w]
        # print(f"Top: {y}, Left: {x}, Width: {w}, Height: {h}")
        word_image_pil = Image.fromarray(word_image)

        text = pytesseract.image_to_string(word_image_pil, config=config)
        # print(text)
        text_center.append([x, y, w, h, text])
        word_image_pil.save(f'word_{i}.jpg')

print(text_center)

print("Words have been extracted and saved as separate images.")


