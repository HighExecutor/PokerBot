import os
import time
import PIL.Image as Image
import PIL.ImageGrab as ImageGrab
import matplotlib.pyplot as plt

img = ImageGrab.grab()
plt.imshow(img)
plt.show()