from selenium import webdriver
import time, os

website_link = "http://suninjuly.github.io/file_input.html"

current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(website_link)

    input_firstname = browser.find_element_by_name("firstname")
    input_firstname.send_keys("Ivan")
    input_lastname = browser.find_element_by_name("lastname")
    input_lastname.send_keys("Petrov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("qqqqqqq")
    input_file = browser.find_element_by_id("file")
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
