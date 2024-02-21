from selenium实战 import webdriver
from selenium实战.webdriver.common.by import By
import time
browser = webdriver.Edge()
browser.get('https://www.baidu.com/')
input_first = browser.find_element(By.ID, 'kw')
input_first.send_keys("妈妈生的，给我学废了")
botton = browser.find_element(By.CLASS_NAME,'bg')
botton.click()
time.sleep(10)
browser.close()