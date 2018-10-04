from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.python.org")
assert "Python" in browser.title
time.sleep(1)
search_box = browser.find_element_by_name("q")
search_box.clear()
search_box.send_keys("pycon")
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in browser.page_source
assert "Estonia" in browser.page_source
time.sleep(5)
browser.close()