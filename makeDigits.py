import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = "img\\bid_digits\\"
name = "9"
img = Image.open(path + name + ".png")
img = img.convert("L").point(lambda x: 0 if x < 200 else 1)
arr = np.array(img).T
np.save(path + name, arr)

plt.imshow(img)
plt.show()

