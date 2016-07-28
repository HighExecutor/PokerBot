import numpy as np
from consts import DIG_ARRS
import matplotlib.pyplot as plt


def bid_rec(img):
    result = ""

    img = img.convert("L").point(lambda x: 0 if x < 200 else 1)
    arr = np.array(img).T

    # plt.imshow(img)
    # plt.show()

    arr_s = arr.shape[0]
    i = 0
    j = 0
    prop = []
    ks = len(DIG_ARRS)
    while i < arr_s:
        row = arr[i]
        if sum(row) == 0:
            i += 1
            continue
        temp_prop = []
        for k in range(ks):
            d_row = DIG_ARRS[k][j]
            if sum(row == d_row) == 12:
                temp_prop.append(k)
        if len(prop) == 0:
            prop = temp_prop
        else:
            prop = [e for e in temp_prop if e in prop]
        if len(prop) == 0:
            i += 1
            j = 0
        elif len(prop) == 1 and j > 0:
            p = prop[0]
            result += str(p)
            dig_arr = DIG_ARRS[p]
            dig_len = dig_arr.shape[0]
            i += dig_len - j
            j = 0
            prop = []
        else:
            i += 1
            j += 1
        pass
    if len(result) == 0:
        return 0
    else:
        return int(result)
