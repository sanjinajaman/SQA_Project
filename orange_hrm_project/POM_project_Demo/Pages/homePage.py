from orange_hrm_project.POM_project_Demo.locators.locators import Locators
from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver=driver
        self.drop_down_by_xpath = Locators.drop_down_by_xpath
        self.logout_btn_xpath = Locators.logout_btn_xpath

        # self.drop_down_by_xpath="/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
        # self.logout_btn_xpath="/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
    def click_dropdown(self):
        self.driver.find_element(By.XPATH, self.drop_down_by_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_btn_xpath).click()

