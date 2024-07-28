# Import required packages
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("./img.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                 cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

file = open("recognized.txt", "w+", encoding="utf-8")
file.write("")
file.close()

def draw_boxes_on_text(img):
    # Return raw information about the detected texts
    raw_data = pytesseract.image_to_data(img)
    for count, data in enumerate(raw_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12:
                x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 1)
                cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255) , 1)
                
    return img

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cropped = im2[y:y + h, x:x + w]
    cv2.imshow('Image', draw_boxes_on_text(cropped))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    file = open("recognized.txt", "a")
    
    text = pytesseract.image_to_string(cropped)
    
    file.write(text)
    file.write("\n")
    
    file.close()
