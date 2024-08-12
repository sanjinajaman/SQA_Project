import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.firefox.service import Service as Firefoxservice

#from webdriver_manager.chrome import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
class GoogleSearch(unittest.TestCase):#inherit the class testcase from unittest
   @classmethod
   def setUpClass(cls):

        #driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
        cls.driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
        #driver.get("file:///D:/1935202505_Sanjina_Jaman/signup.html")
        cls.driver.implicitly_wait(10)  #take 10 second to find elements,,,,,,,this method only needs to be called one time per session
        cls.driver.maximize_window()

   def test_search_automationstepbystep(self):

        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME,"q").send_keys("Automation Step by step")
        self.driver.find_element(By.NAME,"btnK").submit()
        # googleSearchBox=driver.find_element(By.ID,"APjFqb" )
        # googleSearchBox.send_keys("Automation")
        #inter data into textbox
        # driver.find_element(By.NAME,"btnK").submit()

   def automation(self):
       self.driver.get("https://google.com")
       self.driver.find_element(By.NAME, "q").send_keys("Automation")
       self.driver.find_element(By.NAME, "btnK").submit()
   @classmethod
   def tearDownClass(cls):

        # driver.close()
        cls.driver.quit()
        #time.sleep(20) after 20 sec our excution are stoped
        print("Test is completed")


if __name__=="__main__":
    unittest.main()