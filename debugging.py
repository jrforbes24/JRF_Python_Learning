import traceback
import os

"""
Make a box with the given character, height and width. 

************
*          *
*          *
*          *
*          *
************

"""

def makeBox(character, height, width):
    try:        
        if len(character) != 1:
            raise Exception("'character' needs to be a string of length 1")
        if (width < 2) or (height < 2):
            raise Exception('"width" and "height" must be greater or equal to 2.')
        print(character * width)
        for i in range(height - 2):
            print(character + " "*(width - 2) + character)
        print(character * width)
    except:
      errorFile = open('error_log.txt', 'a')  
      errorFile.write(traceback.format_exc())
      errorFile.close()
      print('The traceback info was written to error_log.txt')

makeBox("%",11,12)
    