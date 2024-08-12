from orange_hrm_project.POM_project_Demo.locators.locators import Locators
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver=driver
        self.username_test_box_xpath=Locators.username_test_box_xpath
        self.password_test_box_xpath=Locators.password_test_box_xpath
        self.login_btn=Locators. login_btn
        self.invali_credentials_message_xpath=Locators.invali_credentials_message_xpath

        # self.username_test_box_xpath="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        # self.password_test_box_xpath="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        #self.login_btn="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    def enter_username(self, username):
        self.driver.find_element(By.XPATH,self.username_test_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_test_box_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.username_test_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_test_box_xpath).send_keys(password)

    def enter_login_btn(self):
        self.driver.find_element(By.XPATH,self.login_btn).click()

    def check_invalid(self):
       msg= self.driver.find_element(By.XPATH, self.invali_credentials_message_xpath).text
       return msg