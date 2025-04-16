import requests
theReturnedInfo = requests.get('https://automatetheboringstuff.com/files/rj.txt')
statusCode = theReturnedInfo.status_code
theReturnedInfo.raise_for_status()
if statusCode == 200:
    print('The length of the string:' , str(len(theReturnedInfo.text)))
    playFile = open('RomeoAndJuliet.txt','wb')
    for chunk in theReturnedInfo.iter_content(100000):
        playFile.write(chunk)
    playFile.close
    