from PIL import Image,ImageFilter
import os
img = Image.open('img/wolf.png')
img.thumbnail((300,400))
img.rotate(90)
img.convert(mode='L').save('img/new.png')
img.show()

img.close()

img2 = Image.open('img/new.png')
c = img2.filter(ImageFilter.GaussianBlur()).save('img/blur.png')
img2.show()
