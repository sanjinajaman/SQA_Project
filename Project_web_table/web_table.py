from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.service import Service as  Firefoxservice
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
import pytest
import time

driver=webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://qavbox.github.io/demo/webtable/")
assert "webtable" in driver.title
table=driver.find_element(By.ID,"table01")

'''


#table header part
header=table.find_elements(By.TAG_NAME,"th")

for header_ele in header:
    print(header_ele.text)
'''

'''
#table body
table_body=table.find_elements(By.TAG_NAME, "tbody")


for table_data in table_body:
    print(table_data.text)
'''



'''
#all table row
tbody=table.find_elements(By.TAG_NAME, "td")
rows=table.find_elements(By.TAG_NAME, "tr")
print(len(rows))
for row in rows:
    print(row.text)

'''

'''
#table row
table_body=table.find_element(By.TAG_NAME, "tbody")


rows=table_body.find_elements(By.TAG_NAME, "tr")


print(len(rows))


'''

table_body=table.find_element(By.TAG_NAME, "tbody")

rows=table_body.find_elements(By.TAG_NAME, "tr")


for i in range(len(rows)):
    columns=rows[i].find_elements(By.TAG_NAME, "td")
    for j in range(len(columns)):
        if columns[j].text=="TFS":
            columns[0].click()



print(driver.find_element(By.XPATH, "/html/body/form/fieldset/div/table/tbody/tr[2]/td[2]").text)



# driver.quit()