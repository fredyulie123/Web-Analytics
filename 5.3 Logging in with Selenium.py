"""
This script demonstrates how to use Selenium to open a webpage, log in, and logout
"""

# 1. import useful libraries
from selenium import webdriver
import time

# 2.1 Open an instance of the Chrome browser
browser = webdriver.Chrome("/Users/apostolosfilippas/misc/chromedriver" )

# 2.2 set implicit wait to 10 seconds
#     this tells the browser to wait for that time before throwing an exception
#     allowing us to not get an error when websites take "too long" too load
browser.implicitly_wait(10)

# 2.3 visit the website
browser.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

# 3.1 Enter the username in the appropriate input box
browser.find_element_by_id("txtUsername").send_keys("Admin")
time.sleep(2)
# 3.2 Enter the password in the appropriate input box
browser.find_element_by_id("txtPassword").send_keys("admin123")
time.sleep(2)
# 3.3 Press the log in button
browser.find_element_by_id("btnLogin").click()
time.sleep(2)
# 3.4 Click on the welcome button
browser.find_element_by_id("welcome").click()
time.sleep(2)
# 3.5 Logout
browser.find_element_by_link_text("Logout").click()
time.sleep(2)

# close the browser
browser.close()
browser.quit()

