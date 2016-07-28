import os
import time
import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt
from utils.cursor import *
import random as rnd
from consts import *
from utils.prntscr import *
from utils.digrec import *
from pytesser import pytesser as tesseract


# Main
def main_scenario():
    sit_on_table()
    delay(1.0)
    active = wait_for_action()
    if active:
        context = define_context()
        delay(1.0)
    else:
        print("PIZDA")


def define_context():
    screen = print_screen()

    # cards
    left_card_suit_clr = get_pixel(screen, MY_CARD_LEFT_SUIT[0], MY_CARD_LEFT_SUIT[1])
    right_card_suit_clr = get_pixel(screen, MY_CARD_RIGHT_SUIT[0], MY_CARD_RIGHT_SUIT[1])
    left_card_suit = suit_by_clr(left_card_suit_clr)
    right_card_suit = suit_by_clr(right_card_suit_clr)
    print(left_card_suit_clr)
    print(right_card_suit_clr)
    left_img = card_cut(screen, MY_CARD_LEFT_VAL)
    right_img = card_cut(screen, MY_CARD_RIGHT_VAL)
    left_card_val = CARD_IMG.predict(img_to_arr(left_img))
    right_card_val = CARD_IMG.predict(img_to_arr(right_img))
    cards = [(left_card_val, left_card_suit), (right_card_val, right_card_suit)]
    print("HAND:")
    print(cards)

    # bank
    bank = cut_rec_text(screen, (BANK[0], BANK[1], BANK[2], BANK[3]))
    print("My bank = " + str(bank))

    # bid
    bid_img = img_cut(screen, (MY_BID[0], MY_BID[1], MY_BID[2], MY_BID[3]))
    bid_img.save("temp\\my_bid.png")
    bid = bid_rec(bid_img)


    # Pot
    pot_text = cut_rec_text(screen, (POT[0], POT[1], POT[2], POT[3]))
    print("Pot_text = " + str(pot_text))
    pot = int(pot_text.split(":")[1])
    print("My pot = " + str(pot))

    # stage
    stage = 0
    flop_ping = get_pixel(screen, FLOP_PING[0], FLOP_PING[1])
    print("flop ping: " + str(flop_ping))
    if flop_ping == CARD_FRD_CLR:
        stage = 1
        turn_ping = get_pixel(screen, TURN_PING[0], TURN_PING[1])
        if turn_ping == CARD_FRD_CLR:
            stage = 2
            river_ping = get_pixel(screen, RIVER_PING[0], RIVER_PING[1])
            if river_ping == CARD_FRD_CLR:
                stage = 3
    print("Stage = " + str(stage))

    # table_cards
    table_cards = []
    if stage > 0:
        for f in range(3):
            flop_card_suit_clr = get_pixel(screen, FLOP_CARDS_SUIT[f][0], FLOP_CARDS_SUIT[f][1])
            flop_card_suit = suit_by_clr(flop_card_suit_clr)
            flop_img = card_cut(screen, FLOP_CARDS_VAL[f])
            flop_card_val = CARD_IMG.predict(img_to_arr(flop_img))
            table_cards.append((flop_card_val, flop_card_suit))
        if stage > 1:
            turn_card_suit_clr = get_pixel(screen, TURN_CARD_SUIT[0], TURN_CARD_SUIT[1])
            turn_card_suit = suit_by_clr(turn_card_suit_clr)
            turn_img = card_cut(screen, TURN_CARD_VAL)
            turn_card_val = CARD_IMG.predict(img_to_arr(turn_img))
            table_cards.append((turn_card_val, turn_card_suit))
        if stage > 2:
            river_card_suit_clr = get_pixel(screen, RIVER_CARD_SUIT[0], RIVER_CARD_SUIT[1])
            river_card_suit = suit_by_clr(river_card_suit_clr)
            river_img = card_cut(screen, RIVER_CARD_VAL)
            river_card_val = CARD_IMG.predict(img_to_arr(river_img))
            table_cards.append((river_card_val, river_card_suit))
    print("Table cards = " + str(table_cards))

    active_players = []
    hand_players = []
    dealer = -1
    enemy_banks = []
    enemy_bids = []

    for e in range(5):
        enemy_bank_text = cut_rec_text(screen, ENEMY_BANKS[e])
        enemy_bank = -1
        if "All In" in enemy_bank_text:
            enemy_bank = 0
        else:
            try:
                enemy_bank_test = int(enemy_bank_text.replace("\n", "").replace(",", ""))
                enemy_bank = enemy_bank_test
            except Exception:
                pass
        enemy_banks.append(enemy_bank)

        cards_ping = get_pixel(screen, ACTIVE_PLAYERS_PING[e][0], ACTIVE_PLAYERS_PING[e][1])
        print("Cards ping color = " + str(cards_ping))
        print("Cards FRD color = " + str(CARD_FRD_CLR))
        if min(cards_ping) > 200:
            active_players.append(e)
            hand_players.append(e)
        else:
            border_ping = get_pixel(screen, ENEMY_BORDERS_PING[e][0], ENEMY_BORDERS_PING[e][1])
            if max(border_ping) < 110 and enemy_bank > -1:
                hand_players.append(e)
        # check dealer
        dealer_ping = get_pixel(screen, DEALER_PING[e][0], DEALER_PING[e][1])
        if min(dealer_ping) > 180:
            dealer = e

        # bid recognize
        enemy_bid_img = img_cut(screen, (ENEMY_BIDS[e][0], ENEMY_BIDS[e][1], ENEMY_BIDS[e][2], ENEMY_BIDS[e][3]))
        enemy_bid_img.save("temp\\{0}_bid_img.png".format(e))
        enemy_bid = bid_rec(enemy_bid_img)
        enemy_bids.append(enemy_bid)

    print("Dealer = " + str(dealer))
    print("Hand players = " + str(hand_players))
    print("Active players = " + str(active_players))
    # queue_place
    queue_place = 0
    if dealer == -1:
        queue_place = 0
    else:
        dealer_idx = hand_players.index(dealer)
        queue_place = len(hand_players) - dealer_idx

    screen.save("temp\\debug_screen.png")
    debug_log = open("temp\\debug_log.txt", 'w')
    debug_log.write("Stage = {0}\n".format(stage))
    debug_log.write("My cards = {0}\n".format(cards))
    debug_log.write("My bank = {0}\n".format(bank))
    debug_log.write("Pot = {0}\n".format(pot))
    debug_log.write("My bid = {0}\n".format(bid))
    debug_log.write("Table cards = {0}\n".format(table_cards))
    debug_log.write("Active players = {0}\n".format(active_players))
    debug_log.write("Hand players = {0}\n".format(hand_players))
    debug_log.write("Enemy banks = {0}\n".format(enemy_banks))
    debug_log.write("Enemy bids = {0}\n".format(enemy_bids))
    debug_log.write("Dealer = {0}\n".format(dealer))
    debug_log.write("Queue place = {0}\n".format(queue_place))
    debug_log.close()
    return stage, cards, bank, pot, bid, table_cards, active_players, hand_players, enemy_banks, dealer, queue_place


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
        text = cut_rec_text(screen, seat)
        if text == 'TAKE':
            move_click(TAKE_SEAT_CLICK[i][0], TAKE_SEAT_CLICK[i][1], 0.1)
        i += 1
