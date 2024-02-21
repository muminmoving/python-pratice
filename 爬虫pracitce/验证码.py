import pytesseract as pt
from PIL import Image

path = "C:/Users/moving/Desktop/海报设计/OIP-C (2).jfif"
image = Image.open(path)
image = image.convert("L")
threshold = 90
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,"1")
result = pt.image_to_string(image)
print(result)
image.show()