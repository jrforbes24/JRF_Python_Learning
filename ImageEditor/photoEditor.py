from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'ImageEditor\\imgs'
pathOut = 'ImageEditor\\editedImgs'

for filename in os.listdir(path):
    print(f"{path}\\{filename}")
    img = Image.open(f"{path}\\{filename}")
    edit = img.filter(ImageFilter.SHARPEN)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    # clean_name splits the file path and takes the root. 
    clean_name = os.path.splitext(filename)[0]    
    edit.save(f'{pathOut}\\{clean_name}_edited.jpg')
    
    
