from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
options=Options()
options.add_experimental_option('detach', True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=Options))


driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://www.linkedin.com")
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.find_element(By.ID, "username").send_keys("xyz@gmail.com")
driver.find_element(By.ID, "password").send_keys(87890456984)

driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
