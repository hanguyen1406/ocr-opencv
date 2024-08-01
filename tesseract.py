from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary


image = Image.open('./word_83.jpg')
config = '--psm 6 -l vie'

text = pytesseract.image_to_string(image, config=config)
# Print the extracted text
print(text)
