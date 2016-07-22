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
    TABLES_LIST = 120, 520
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
    MY_CARD_LEFT_VAL = 589, 488, 605, 568
    MY_CARD_RIGHT_VAL = 656, 488, 670, 568

    FLOP_PING = 651, 272
    TURN_PING = 724, 272
    RIVER_PING = 802, 272

    FLOP_CARDS_SUIT = [(479, 301), (553, 301), (629, 301)]
    TURN_CARD_SUIT = 704, 301
    RIVER_CARD_SUIT = 779, 301

    FLOP_CARDS_VAL = [(472, 273, 488, 295),
                      (546, 272, 563, 294),
                      (622, 273, 639, 294)]
    TURN_CARD_VAL = 697, 274, 713, 292
    RIVER_CARD_VAL = 771, 274, 790, 294

    ACTIVE_PLAYERS_PING = [(222, 351), (222, 120), (618, 33), (1018, 121), (1018, 351)]

    SUIT_COLORS = dict()
    # spades
    SUIT_COLORS[(0, 0, 0)] = 0
    # clubs
    SUIT_COLORS[(32, 128, 0)] = 1
    # diamonds
    SUIT_COLORS[(0, 0, 237)] = 2
    # hearts
    SUIT_COLORS[(200, 8, 200)] = 3

