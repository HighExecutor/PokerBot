import time
from pytesser import pytesser
from PIL import Image
import matplotlib.pyplot as plt
import PIL.ImageOps as ops


filepath = 'D:\Projects\PokerBot\\temp\\2seat.png'
start = time.clock()
img = Image.open(filepath)

# img = img.convert('L')
# img = ops.grayscale(img)
# img = ops.invert(img)

# img = img.point(lambda x: 0 if x < 128 else 255, '1')

text = pytesser.image_file_to_string(filepath)
# text = pytesser.image_to_string(img)
fin = time.clock()
print("Time = " + str(fin - start))
print text

plt.imshow(img)
plt.show()