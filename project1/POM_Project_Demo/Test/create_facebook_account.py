from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com")
act=ActionChains(driver)
#act.click(driver.find_element(By.XPATH,"//a[text()='Create New Account']")).perform()
driver.find_element(By.PARTIAL_LINK_TEXT, "Create new account").click()
#driver.find_element(By.ID,"u_0_0_4U").click()
#time.sleep(20)
driver.find_element(By.NAME,"firstname").send_keys("tanjina")
driver.find_element(By.NAME, "lastname").send_keys("tanji")
#driver.find_element(By.NAME, "reg_email__").send_keys("01301778262")
driver.find_element(By.NAME,"reg_email__").send_keys("01301778262")
driver.find_element(By.ID,"password_step_input").send_keys("jnina_jni_na_12345A@")
day=Select(driver.find_element(By.NAME,"birthday_day"))
day.select_by_visible_text("10")
month=Select(driver.find_element(By.NAME,"birthday_month"))
month.select_by_visible_text("Jun")


year=Select(driver.find_element(By.NAME,"birthday_year"))
year.select_by_visible_text("2001")
driver.find_element(By.CLASS_NAME,"_58mt").click()

driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()



# driver.find_element(By.ID, "email").send_keys("xyz")
# driver.find_element(By.ID, "pass").send_keys(87890456984)
#driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").submit()
#driver.find_element(By.ID, "u_0_5_DZ").click()
