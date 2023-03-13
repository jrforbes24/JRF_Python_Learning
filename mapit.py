#! python
import webbrowser,sys,pyperclip

# get the args from the command line if passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) 
# get if they are on the clipboard
else:
    address = pyperclip.paste()

# Open a new tab in Chrome
webbrowser.open('https://www.google.com/maps/place/'+ address)

