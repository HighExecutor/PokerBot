import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt

def print_screen():
    img = ImageGrab.grab()
    return img

def img_cut(img, points):
    return img.crop(points)