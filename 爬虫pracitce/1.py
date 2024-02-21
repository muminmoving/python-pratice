from selenium实战 import webdriver
from selenium实战.webdriver.common.by import By
import time
i = input('输入你想搜索的内容')
browser = webdriver.Edge()
browser.get('https://www.baidu.com/')
input_first = browser.find_element(By)
print(input_first)