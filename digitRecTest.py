import time
from pytesser import pytesser
from PIL import Image
import matplotlib.pyplot as plt
import PIL.ImageOps as ops


filepath = 'pokerTest.png'
# start = time.clock()
img = Image.open(filepath)
#
# # img = ops.grayscale(img)
# # img = ops.invert(img)
# # img = img.convert('LA')
# fin = time.clock()
# print("Preprocess time = " + str(fin - start))
# start = time.clock()

# fin = time.clock()
# print("Show time = " + str(fin - start))

start = time.clock()
text = pytesser.image_file_to_string(filepath)
fin = time.clock()
print("Time = " + str(fin - start))
print text

plt.imshow(img)
plt.show()