from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import requests
import pandas as pd



driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.maximize_window()
URL="https://www.amazon.com/stores/page/328FEA96-5336-4347-AC04-42FB363034A8"
driver.get(URL)
HEADERS = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

webpage=requests.get(URL, headers=HEADERS)
print(webpage)
# print(webpage.content)
print(type(webpage.content))

# Soup object containing all  data
soup=BeautifulSoup(webpage.content, "html.parser")
print(soup)
