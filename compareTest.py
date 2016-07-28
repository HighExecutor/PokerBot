from PIL import Image, ImageChops
import os
import matplotlib.pyplot as plt
from pytesser import pytesser as tesseract
import PIL.ImageOps as ops
import numpy as np
from utils.prntscr import *
# from consts import *

path = "temp\\"
file = "debug_screen"
# path = "img\\"
# file = "card_test"

f1 = Image.open(path + file + ".png")
# f11 = f1.convert("L")
f11 = f1.point(lambda x: 0 if x < 200 else 1)
arr1 = np.array(f11)
print()
# pred = CARD_IMG.predict(arr1)
# print(pred)

# arr1 = np.array(Image.open(path + "card.png").convert("L").point(lambda x: 0 if x < 255 else 255, "1"))
# arr2 = np.array(Image.open(path + "cards\\l7672.png").convert("L").point(lambda x: 0 if x < 255 else 255, "1"))

# arrM = arr2.reshape(400)
# start = time.clock()
# for _ in range(50):
#     pred = CARD_IMG.predict(arrM)
#     print("predict = " + str(pred))


# print(rec_card(f1))
# print(is_equal_arr(arr2, arr2))


# arr1 = np.array(f1)
# arr2 = np.array(f2)
#
plt.subplot(311)
plt.imshow(f1)
plt.subplot(313)
plt.imshow(f11)
plt.show()
# plt.subplot(313)
# diff = ImageChops.difference(f1, f2)
# plt.imshow(diff)
# plt.show()

# print(f1 == f2)
#
# res = True
# for i in range(20):
#     for j in range(20):
#         if arr1[i, j] != arr2[i, j]:
#             res = False
#             break
# print(res)
# text1 = tesseract.image_to_string(f1)
# text2 = tesseract.image_to_string(f2)
# print("T1:" + text1)
# print("T2:" + text2)

pass
