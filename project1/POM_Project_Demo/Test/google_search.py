import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.firefox.service import Service as Firefoxservice

#from webdriver_manager.chrome import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

#driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
#driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
driver.implicitly_wait(10)  #take 10 second to find elements,,,,,,,this method only needs to be called one time per session
driver.maximize_window()
driver.get("https://google.com")
driver.find_element(By.NAME,"q").send_keys("Automation Step by step")
driver.find_element(By.NAME,"btnK").submit()
# googleSearchBox=driver.find_element(By.ID,"APjFqb" )
# googleSearchBox.send_keys("Automation")
#inter data into textbox
# driver.find_element(By.NAME,"btnK").submit()
# driver.close()
# driver.quit()
#time.sleep(20) after 20 sec our excution are stoped