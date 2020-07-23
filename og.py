from PIL import Image, ImageFilter
import os

#Sample image dimension: (1276,876)
from os import listdir

transparent_bg = Image.open('D:\\Aniket\\Documents\GitHub\\Certificate-Edit\\default\\transparent.png')

basewidth = 1276
img = Image.open('D:\\Aniket\\Documents\\GitHub\\Certificate-Edit\\injest\\asd.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
new_img = img.resize((basewidth,hsize), Image.ANTIALIAS)

w1, h1 = transparent_bg.size
w2, h2 = new_img.size

w1c = int(w1/2)
h1c = int(h1/2)

w2c = int(w2/2)
h2c = int(h2/2)

wo = w1c - w2c
ho = h1c - h2c
size = (wo,ho)
print(size)

# drop_shadow(new_img).show()

transparent_bg.paste(new_img,size)
transparent_bg.show()
