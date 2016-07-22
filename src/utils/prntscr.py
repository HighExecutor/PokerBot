import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt
import win32gui
import time


def print_screen():
    img = ImageGrab.grab()
    return img


def img_cut(img, points):
    return img.crop(points)


def get_pixel(img, x, y):
    return img.getpixel((x, y))
