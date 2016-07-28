from PIL import Image
import numpy as np
import os

print("Resources loading")

home = True

if not home:
    WINDOW_START_POSITION = 1080, 200
    # button to expand table window
    TABLE_EXP = 1790, 500
    # middle in the list of tables
    TABLES_LIST = 100, 400
    # place to click for sit on the table
    TAKE_SEAT_CLICK = [(895, 778), (402, 618), (402, 330), (895, 221), (1394, 331), (1394, 619)]
    # place with text "TAKE"
    TAKE_SEAT = [(924, 744, 985, 763),
                 (430, 583, 493, 604),
                 (430, 296, 492, 317),
                 (922, 187, 985, 206),
                 (1421, 297, 1484, 317),
                 (1421, 584, 1482, 602)]

else:
    WINDOW_START_POSITION = 1180, 200
    TABLE_EXP = 1225, 190
    TABLES_LIST = 120, 400
    TAKE_SEAT_CLICK = [(625, 579), (230, 450), (230, 220), (593, 135), (1024, 219), (1025, 450)]
    TAKE_SEAT = [(644, 547, 699, 564),
                 (248, 419, 304, 438),
                 (248, 189, 305, 208),
                 (645, 101, 698, 118),
                 (1042, 190, 1097, 208),
                 (1043, 419, 1098, 437)]
    OK_TO_SIT = 586, 342

    ACTIVE_BORDER_PIXEL = 568, 537
    ACTIVE_BORDER_COLOR = (223, 223, 223)

    MY_CARD_LEFT_SUIT = 597, 517
    MY_CARD_RIGHT_SUIT = 663, 517
    MY_CARD_LEFT_VAL = 589, 487
    MY_CARD_RIGHT_VAL = 655, 487

    FLOP_PING = 651, 272
    TURN_PING = 724, 272
    RIVER_PING = 802, 272

    CARD_FRD_CLR = (255, 255, 255)

    FLOP_CARDS_SUIT = [(479, 301), (553, 301), (629, 301)]
    TURN_CARD_SUIT = 704, 301
    RIVER_CARD_SUIT = 779, 301

    FLOP_CARDS_VAL = [(471, 273), (546, 273), (621, 273)]
    TURN_CARD_VAL = 696, 273
    RIVER_CARD_VAL = 771, 273

    ACTIVE_PLAYERS_PING = [(222, 351), (222, 120), (618, 33), (1018, 121), (1018, 351)]

    # Card value recognition
    x_card = []
    y_card = []
    from sklearn.svm import SVC

    CARD_IMG = SVC(kernel='linear')
    for i in range(13):
        idx = i + 2
        path = "D:\\Projects\\PokerBot\\img\\cards\\" + str(idx) + "\\"
        cards = os.listdir(path)
        for c in cards:
            img = Image.open(path + c)
            img = img.convert("L").point(lambda x: 1 if x < 100 else 0)
            x = np.array(img).reshape(400)
            y = i + 2
            x_card.append(x)
            y_card.append(y)
    x_card = np.array(x_card)
    y_card = np.array(y_card)
    CARD_IMG.fit(x_card, y_card)

    BANK = 642, 572, 733, 594
    POT = 561, 233, 760, 257

    MY_BID = 550, 435, 740, 447

    ENEMY_BORDERS_PING = [(200, 410), (200, 180), (594, 92), (1025, 180), (1036, 410)]
    ENEMY_BANKS = [(178, 445, 281, 466),
                   (178, 214, 281, 236),
                   (575, 128, 676, 149),
                   (1025, 215, 1125, 236),
                   (1025, 443, 1124, 466)]
    DEALER_PING = [(395, 432), (362, 255), (574, 185), (956, 262), (911, 432)]

    ENEMY_BIDS = [(375, 396, 510, 408),
                  (400, 230, 510, 242),
                  (530, 186, 750, 198),
                  (750, 230, 900, 242),
                  (770, 397, 920, 409)]

    # bid digits
    digits_path = "D:\\Projects\\PokerBot\\img\\bid_digits\\"
    DIG_ARRS = []
    for d in range(10):
        d_img = np.load(digits_path + str(d) + ".npy")
        DIG_ARRS.append(d_img)

print("Resources have been loaded")