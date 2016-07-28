import time
from pytesser import pytesser
from PIL import Image
import matplotlib.pyplot as plt
import PIL.ImageOps as ops
import numpy as np
from utils.prntscr import *
from consts import *

filepath = 'D:\Projects\PokerBot\\temp\\debug_screen.png'
start = time.clock()
screen = Image.open(filepath)
img = img_cut(screen, (ENEMY_BANKS[2]))

# img = img.convert("L").point(lambda x: 0 if x < 120 else 255)
# arr = np.array(img)
# arr.save("D:\Projects\PokerBot\\img\\bid_digits\\1.npy")

# img = img.convert('L')
# img = ops.grayscale(img)
# img = ops.invert(img)
# img = img.point(lambda x: 0 if x < 128 else 255, '1')

# text = pytesser.image_file_to_string(filepath, graceful_errors=True)
img.save("D:\Projects\PokerBot\\temp\\temp.png")
# text = pytesser.image_to_string(img)
text = pytesser.image_file_to_string("D:\Projects\PokerBot\\temp\\temp.png")

# text = pytesser.image_to_string(img)

fin = time.clock()
print("Time = " + str(fin - start))
print text
# text2 = int(text.replace("\n", "").replace(",", ""))
# print(text2)

plt.imshow(img)
plt.show()