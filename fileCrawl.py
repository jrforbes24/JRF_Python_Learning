import os
from PIL import Image
import shutil
import time


for foldername, subfolders, filenames in os.walk('C:\\Users\\johnr\\Pictures'):
    for file in filenames:
        imagePath = os.path.join(foldername,file)
        
        stat_info = os.stat(imagePath)
        ctime = stat_info.st_ctime
        ctime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ctime))
        print(f"For the {file} the creation time is: {ctime_str}")
        userId = stat_info.st_uid
        print(f"For the {file} the userId is: {userId}")
        
        
        try:
            with Image.open(imagePath) as img:
                format = img.format
                print(f"For the {file} the image format is: {format}")
               
        except Exception as e:
            print(f"An error occurred: {e}")
            
        
        


    

    