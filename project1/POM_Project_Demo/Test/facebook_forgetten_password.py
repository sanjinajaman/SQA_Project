from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

import time
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com")

driver.find_element(By.ID, "email").send_keys("xyz")
driver.find_element(By.ID, "pass").send_keys(87890456984)

driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten password?").click()
#click(driver.find_element(By.ID, "u_0_5_8J")).per
