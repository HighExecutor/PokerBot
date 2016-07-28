from PIL import Image

img = Image.open("img\\card.png").convert('L').point(lambda x: 0 if x < 255 else 255, '1')
img.save("img\\cards\\14.png")
