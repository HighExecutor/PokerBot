import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt
from pytesser import pytesser as tesseract
import numpy as np


def print_screen():
    img = ImageGrab.grab()
    return img


def img_cut(img, points):
    return img.crop(points)


def card_cut(img, point):
    temp = img.crop((point[0], point[1], point[0] + 20, point[1] + 20))
    return temp


def get_pixel(img, x, y):
    return img.getpixel((x, y))


def cut_rec_text(img, rect):
    cut = img_cut(img, rect)
    path = "temp/temp.png"
    cut.save(path)
    text = tesseract.image_file_to_string(path, graceful_errors=True)
    text = text.replace(" ", "").replace("\n", "").replace(",", "").replace(".", "")
    return text


def rec_text(path):
    text = tesseract.image_file_to_string(path, graceful_errors=True)
    text = text.replace(" ", "").replace("\n", "").replace(",", "")
    return text


def is_equal_arr(arr1, arr2):
    for i in range(20):
        for j in range(20):
            if arr1[i, j] != arr2[i, j]:
                return False
    return True


def img_convert(img):
    return img.convert("L").point(lambda x: 1 if x < 100 else 0)


def img_to_arr(img):
    im = np.array(img_convert(img)).reshape(400)
    return im


def suit_by_clr(pixel):
    max_v = max(pixel)
    argmax = np.argmax(pixel)
    if max_v < 20:
        return 0
    elif argmax == 0:
        return 3
    elif argmax == 1:
        return 1
    else:
        return 2