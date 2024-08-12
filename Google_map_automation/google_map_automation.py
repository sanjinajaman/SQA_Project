from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

driver.get("https://www.google.com/maps/@23.7031975,90.421438,15z?entry=ttu")

driver.maximize_window()
driver.implicitly_wait(10)
def searchplace():
        driver.find_element(By.ID,"searchboxinput").send_keys("shutrapur")
        search=driver.find_element(By.ID, "searchbox-searchbutton")
        search.click()

searchplace()


def directions():
    sleep(10)
    direction=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span")
    direction.click()
directions()

def find():
    sleep(10)
    find=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys("gandaria")
find()

def search_destination():
    sleep(5)
    search_destination=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search_destination.click()

search_destination()


def pannel():
   act=ActionChains(driver)
   act.click(driver.find_element(By.CLASS_NAME, "EIbCs")).perform()

pannel()
def kilometers():
    sleep(3)
    Totalkilometers=driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/div")
    print("TotalKilometers:", Totalkilometers.text)
    sleep(5)
    time=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[1]")

    print("Total Time:",time.text)

kilometers()





















