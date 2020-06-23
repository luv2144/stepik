from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

website_link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(website_link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input_y = browser.find_element_by_id("answer")
    input_y.send_keys(str(y))
    checkbox_item = browser.find_element_by_id("robotCheckbox")
    checkbox_item.click()
    radiobutton_item = browser.find_element_by_id("robotsRule")
    radiobutton_item.click()
    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
