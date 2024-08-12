from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

import time
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.get("https://www.linkedin.com")
assert "LinkedIn" in driver.title
sign_in_button = find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in_button.click()
assert "Sign In" in driver.title
#driver.quit()


driver.get("https://www.linkedin.com/login")
email_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
sign_in_button = driver.find_element_by_xpath("//button[@type='submit']")

email_field.send_keys("valid_email@example.com")
password_field.send_keys("valid_password")
sign_in_button.click()

assert "Feed" in driver.title or "Profile" in driver.title
driver.quit()