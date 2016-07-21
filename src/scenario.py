import os
import time
import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt
from utils.cursor import *
import random as rnd
from points import *
from utils.prntscr import *
from pytesser import pytesser as tesseract


def test(i):
    print(i)
    img = ImageGrab.grab()
    img.save('temp/' + str(i) + ".png")

def sit_on_table():
    move(TABLES_LIST[0], TABLES_LIST[1] + rnd.randint(0, 40))
    double_click()
    time.sleep(0.5)
    move_click(TABLE_EXP[0], TABLE_EXP[1], 0.5)
    delay(1.0)
    find_seat()

def find_seat():
    screen = print_screen()
    i = 0
    for seat in TAKE_SEAT:

        chair = img_cut(screen, seat)
        path = "temp/" + str(i) + "seat.png"
        chair.save(path)
        text = tesseract.image_file_to_string(path).replace(" ", "").replace("\n", "")
        if text == 'TAKE':
            move_click(TAKE_SEAT_CLICK[i][0], TAKE_SEAT_CLICK[i][1], 0.1)
        i += 1


