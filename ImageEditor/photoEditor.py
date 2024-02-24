from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'ImageEditor\imgs'
pathOut = 'ImageEditor\editedImgs'

for filename in os.listdir(path):
    print(filename)
