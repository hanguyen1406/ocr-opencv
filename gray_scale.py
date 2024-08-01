from PIL import Image
img = Image.open("./img.jpg")

# If you want a greyscale image, simply convert it to the L (Luminance) mode:
new_img = img.convert('L')


new_img.save('./cleaned_text.png')