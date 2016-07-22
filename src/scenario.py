import os
import time
import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt
from utils.cursor import *
import random as rnd
from consts import *
from utils.prntscr import *
from pytesser import pytesser as tesseract


def test(i):
    print(i)
    img = ImageGrab.grab()
    img.save('temp/' + str(i) + ".png")


# Main
def main_scenario():
    sit_on_table()
    delay(1.0)
    active = wait_for_action()
    if active:
        for _ in range(100000):
            context = define_context()
            delay(1.0)
    else:
        print("PIZDA")


def define_context():
    screen = print_screen()
    # cards
    left_card_suit_clr = get_pixel(screen, MY_CARD_LEFT_SUIT[0], MY_CARD_LEFT_SUIT[1])
    right_card_suit_clr = get_pixel(screen, MY_CARD_RIGHT_SUIT[0], MY_CARD_RIGHT_SUIT[1])
    left_card_suit = SUIT_COLORS[left_card_suit_clr]
    right_card_suit = SUIT_COLORS[right_card_suit_clr]




    # bank
    # bid
    # Pot
    # stage
    # queue_place
    # active_players
    # table_cards


def wait_for_action():
    found = False
    for i in range(500):
        screen = print_screen()
        delay(0.1)
        pixel = get_pixel(screen, ACTIVE_BORDER_PIXEL[0], ACTIVE_BORDER_PIXEL[1])
        if pixel==ACTIVE_BORDER_COLOR:
            found = True
            break
        else:
            delay(1.0)
    return found


def sit_on_table():
    delay(1.0)
    move(TABLES_LIST[0], TABLES_LIST[1] + rnd.randint(0, 40))
    double_click()
    time.sleep(2.0)
    move_click(TABLE_EXP[0], TABLE_EXP[1], 2.0)
    delay(2.0)
    find_seat()
    delay(1.0)
    move_click(OK_TO_SIT[0], OK_TO_SIT[1])


def find_seat():
    screen = print_screen()
    i = 0
    for seat in TAKE_SEAT:
        chair = img_cut(screen, seat)
        path = "temp/" + str(i) + "seat.png"
        chair.save(path)
        text = tesseract.image_file_to_string(path, graceful_errors=True).replace(" ", "").replace("\n", "")
        if text == 'TAKE':
            move_click(TAKE_SEAT_CLICK[i][0], TAKE_SEAT_CLICK[i][1], 0.1)
        i += 1
