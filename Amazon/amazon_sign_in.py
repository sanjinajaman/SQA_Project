'''
1.Login Automation
2. Product search
3.Add to cart automation'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/ap/signin?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Faut"
           "h%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Drhf_sign_in&openid.assoc_handle=usflex&openid.pape.max_auth_age=0")
driver.find_element(By.ID,"ap_email").send_keys("xyz@gmail.com")
#driver.find_element()