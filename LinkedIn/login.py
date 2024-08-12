from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

import time
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://www.linkedin.com")
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.find_element(By.ID, "username").send_keys("xyz@gmail.com")
driver.find_element(By.ID, "password").send_keys(87890456984)

#driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

