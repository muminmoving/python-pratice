import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
# 转至搜索页面
browser = webdriver.Edge()
wait = WebDriverWait(browser, 10)
def get_page(page):
    try:
        url = 'https://s.taobao.com/search?q='+quote('泡面')
        browser.get(url)
        if page > 1:
            input = wait.until(
            EC.presence_of_element_located(
            (By.XPATH, "//span[@name='next-input next-medium next-pagination-jump-input']/input")))
            submit = wait.until((
            EC.element_to_be_clickable(By.XPATH, "//div[@class='next-pagination-pages']/botton[@class=next-btn]")
            ))
            input.send_keys(page)
            submit.click()
            input.clear()
    except TimeoutException:
        get_page(page)

get_page(2)
time.sleep(4)