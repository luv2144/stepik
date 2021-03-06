from selenium import webdriver
import time, math

website_link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(website_link)

    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    result = calc(int(x))
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(str(result))
    new_page_button = browser.find_element_by_css_selector("[type=\"submit\"]")
    new_page_button.click()

finally:
    time.sleep(10)
    browser.quit()
