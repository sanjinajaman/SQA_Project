from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

from time import sleep
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

#driver=webdriver.Firefox()

#open amazon ulr
driver.get("https://www.amazon.in/")
# enter data on search bar
add_to_cart=driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone 15 pro max")
# click on search button
driver.find_element(By.ID, "nav-search-submit-button").click()
#display iphone pro max details
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span").click()
#switch to the new tab
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone+15+pro+max&qid=1703107535&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

#click on add to cart
driver.find_element(By.ID,"add-to-cart-button").click()

#wait for a while to see the changes
sleep(10)

