from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
import datetime
import sys
import pytest

base_url = ("https://facebook.com")
driver = webdriver.Chrome(".\chromedriver")



driver.get(base_url)
driver.maximize_window()
username = driver.find_element_by_id("Username")
password = driver.find_element_by_id("Password")
username.send_keys("username")
password.send_keys("pass")
driver.save_screenshot(".\Path to folder\landing_page.png")
driver.find_element_by_link_text('Logout').click()

driver.quit()
