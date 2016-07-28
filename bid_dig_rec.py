import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from consts import *
from utils.digrec import *
from utils.prntscr import *


result = ""
screen = Image.open("temp\\debug_screen.png")
bid_img = img_cut(screen, (MY_BID))
recognize = bid_rec(bid_img)
print("res = " + str(recognize))

for e in range(5):
    enemy_bid_img = img_cut(screen, (ENEMY_BIDS[e]))
    enemy_rec = bid_rec(enemy_bid_img)
    print("{0} res = {1}".format(e, enemy_rec))

# plt.imshow(bid_img.convert("L").point(lambda x: 0 if x < 200 else 1))
# plt.imshow(my_bid2)
# plt.show()