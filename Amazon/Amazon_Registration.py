from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.get("https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.mode=checkid_setup&openid.ns=http://specs.openid.net/auth/2.0&openid.ns.pape=http://specs.openid.net/extensions/pape/1.0&openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.com/gp/yourstore/home?ie%3DUTF8%26ref_%3Dnav_newcust")
#enter first and last name
driver.find_element(By.ID, "ap_customer_name").send_keys("Sanjina Jaman")
#enter email or phone number
driver.find_element(By.ID, "ap_email").send_keys("sanjinajaman.softdev@gmail.com")
#enter password
driver.find_element(By.ID, "ap_password").send_keys("*************")
#re-type password
driver.find_element(By.ID, "ap_password_check").send_keys("*************")
#driver.find_element(By.ID, "continue").click()