from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


# open firefox
browser = webdriver.Firefox()
# go to url python.org
browser.get('https://www.python.org/')
browser.implicitly_wait(10)
elem = browser.find_element(by=By.CSS_SELECTOR,value ='#downloads > a')
elem.click
browser.implicitly_wait(30)
