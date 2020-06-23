from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math

website_link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(website_link)

    x = browser.find_element_by_id("input_value").text
    result = calc(int(x))
    input_result = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_result)
    input_result.send_keys(str(result))
    checkbox_item = browser.find_element_by_id("robotCheckbox")
    checkbox_item.click()
    radiobutton_item = browser.find_element_by_id("robotsRule")
    radiobutton_item.click()
    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()