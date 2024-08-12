from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

import time
import HtmlTestRunner
import unittest
#import below 3 lines for run the code in command line
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))

from orange_hrm_project.POM_project_Demo.Pages.login_page import LoginPage
from orange_hrm_project.POM_project_Demo.Pages.homePage import HomePage




class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_01_login_valid(self):
        driver=self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.enter_login_btn()
        homepage=HomePage(driver)
        homepage.click_dropdown()
        homepage.logout()
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        # #driver.find_element(By.name, "username").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        #
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        #
        # click=self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p")
        # click.click()
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

    def test_02_login_invalid_username(self):
            driver = self.driver

            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            login = LoginPage(driver)
            login.enter_username("Admin1")
            login.enter_password("admin12")
            login.enter_login_btn()
            message=driver.find_element(By.XPATH,"").text
            self.assertEqual(message,"Invalid credentials")

    @classmethod
    def tearDown(self) :
        self.driver.close()
        self.driver.quit()
        print("Test is completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/user/PycharmProjects/SQA_Project/reports'))