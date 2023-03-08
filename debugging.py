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
    if len(character) != 1:
        raise Exception("'character' needs to be a string of length 1")
    print(character * width)
    for i in range(height - 2):
        print(character + " "*(width - 2) + character)
    print(character * width)

makeBox("##",5,125)
    