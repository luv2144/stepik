from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

website_link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(website_link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button_book = browser.find_element_by_id("book")
    button_book.click()
    # browser.execute_script("return arguments[0].scrollIntoView(true);")
    x = browser.find_element_by_id("input_value").text
    result = calc(int(x))
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(str(result))
    button_submit = browser.find_element_by_id("solve")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
