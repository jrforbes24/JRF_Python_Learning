import bs4
import requests

def webScraping(theURL):
    res = requests.get(theURL)
    # res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')    
    elements = soup.select('#calibre_link-25 > div > p:nth-child(2) > a')
    return(elements[0].text.strip())






print('The youtube link text is:',webScraping('https://automatetheboringstuff.com/chapter2/'))