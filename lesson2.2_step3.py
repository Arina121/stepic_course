import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text

    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(num1) + int(num2)))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
