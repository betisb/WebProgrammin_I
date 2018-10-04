from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://bbaheri.pythonanywhere.com/login")
assert "Sign In" in browser.page_source
assert "Username" in browser.page_source
assert "Password" in browser.page_source
time.sleep(1)
submit_button = browser.find_element_by_name("submit")
submit_button.click()
assert "field is required" in browser.page_source
username_text = browser.find_element_by_name("username")
password_text = browser.find_element_by_name("password")
username_text.clear()
username_text.send_keys("John")
password_text.clear()
password_text.send_keys("password")
time.sleep(5)
submit_button = browser.find_element_by_name("submit")
submit_button.click()
assert "Login requested" in browser.page_source
assert "Beautiful day in Portland" in browser.page_source
assert "How Are you?" in browser.page_source
time.sleep(5)
browser.close()