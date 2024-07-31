from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary


image = Image.open('./word_4.jpg')

text = pytesseract.image_to_string(image, lang='vie')
# Print the extracted text
print(text)
