from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains

import time
driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))

# Initialize the WebDriver (assuming Firefox in this example)
driver = webdriver.Firefox()

# Open the first tab
driver.get("https://www.amazon.in/")
add_to_cart = driver.find_element(By.ID, "twotabsearchtextbox")
add_to_cart.send_keys("iphone 15 pro max")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()

# Open a new tab using JavaScript
#driver.execute_script("window.open('', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone%2B15%2Bpro%2Bmax&qid=1703075272&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

# Do some actions in the second tab
driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()



# Wait for a while to see the changes
sleep(2)

# Switch back to the first tab
# driver.switch_to.window(driver.window_handles[0])

# Perform actions in the first tab
# search_box = driver.find_element("name", "q")
# search_box.send_keys("Python automation")
# search_box.submit()

# Wait for a while to see the changes
# sleep(2)

# Close the browser
# driver.quit()