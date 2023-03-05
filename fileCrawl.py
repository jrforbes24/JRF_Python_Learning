import os
from PIL import Image
import shutil


for foldername, subfolders, filenames in os.walk('C:\\Users\\johnr\\Pictures'):
    for file in filenames:
        imagePath = os.join(foldername,file)
        
        


    

    