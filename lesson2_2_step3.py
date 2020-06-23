from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

website_link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(website_link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    answer = int(num1.text) + int(num2.text)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(answer))

    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()