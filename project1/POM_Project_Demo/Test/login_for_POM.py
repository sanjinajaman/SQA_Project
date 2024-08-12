from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from project1.POM_Project_Demo.Pages.login_page import LoginPage
import unittest
import time


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://www.facebook.com")
        login=LoginPage(driver)
        login.enter_username("Admin")
        login.password_textbox_id("kjdftiufdj")

        login.enter_login_btn()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print("Test completed")


if __name__ == '__main__':
    unittest.main()


