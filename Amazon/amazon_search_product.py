from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://www.amazon.in/")

#search product
''' 
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone")
driver.find_element(By.ID,"nav-search-submit-button").click()

driver.find_element(By.ID, "twotabsearchtextbox").send_keys(" 14 pro")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()

'''

#multiple item search
'''
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(" phone, camera")
driver.find_element(By.ID,"nav-search-submit-button").click()


'''


#missplled item name
'''
driver.find_element(By.ID,"twotabsearchtextbox").send_keys(" phne")
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()

'''







#NAGATIVE TEST CASE






add_to_cart = driver.find_element(By.ID, "twotabsearchtextbox")
add_to_cart.send_keys("iphone 15 pro max")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()


allTabs=driver.window_handles
print(allTabs)

for tab in allTabs:
    driver.switch_to.window(tab)
    print(driver.current_url)
    # if(driver.current_url=="https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone%2B15%2Bpro%2Bmax&qid=1703090385&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"):
    #      driver.find_element(By.Id,"add-to-cart-button").click()



# driver.get("https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone%2B15%2Bpro%2Bmax&qid=1703075272&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
# act=ActionChains(driver)
# act.click(driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')).perform()




'''
driver.get("https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone%2B15%2Bpro%2Bmax&qid=1703075272&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
print(driver.current_url)
'''














#Purchasing (add to cart)
# def addtocat():
#
#     add_to_cart = driver.find_element(By.ID, "twotabsearchtextbox")
#     add_to_cart.send_keys("iphone 15 pro max")
#     driver.find_element(By.ID, "nav-search-submit-button").click()
#
# addtocat()
#
#
# def display_product():
#     driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()
#
# display_product()
#
#
# def addcart():
#     driver.get("https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone%2B15%2Bpro%2Bmax&qid=1703075272&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
#     act=ActionChains(driver)
#     act.click(driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')).perform()
#
# addcart()
#driver.get("https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHX68YG9/ref=sr_1_1_sspa?keywords=iphone+15+pro+max&qid=1703013750&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
#driver.find_element(By.ID, "add-to-cart-button").click()









