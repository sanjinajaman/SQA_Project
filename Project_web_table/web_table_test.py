from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
# import pytest
import time

driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://qavbox.github.io/demo/webtable/")
assert "webtable" in driver.title
table=driver.find_element(By.ID,"table01")
header=table.find_elements(By.TAG_NAME,"th")

for header_ele in header:
    print(header_ele.text)

driver.quit()