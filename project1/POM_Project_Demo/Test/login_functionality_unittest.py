from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
            cls.driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)


    def test_login_valid(self):
            self.driver.get("https://www.facebook.com")
            self.driver.find_element(By.ID, "email").send_keys("xyz")
            self.driver.find_element(By.ID, "pass").send_keys(87890456984)
            self.driver.find_element(By.NAME, 'login').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print("Test completed")


if __name__=='__main__':
    unittest.main()
    

