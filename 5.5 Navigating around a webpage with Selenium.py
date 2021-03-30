"""
This script demonstrates how to use Selenium to open a webpage, and navigate around it
"""

# 1. import useful libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 2.1 Open an instance of the Chrome browser
browser = webdriver.Chrome("/Users/apostolosfilippas/misc/chromedriver" )

# 2.2 set implicit wait to 10 seconds
#     this tells the browser to wait for that time before throwing an exception
#     allowing us to not get an error when websites take "too long" too load
browser.implicitly_wait(10)

# 2.3 visit the website
browser.get("https://docs.seleniumhq.org")
time.sleep(2)

# 3.1 Go to Download
element = browser.find_element_by_link_text("Download")

# element contains some useful information
element.tag_name
element.text
element.location
element.get_attribute('href')

# click on "Download" button
element.click()
time.sleep(2)


# 3.2 Go to Projects (a little fast)
browser.find_element_by_link_text("Projects").click()
time.sleep(2)


# 3.3 Enter "some google search" on the search bar and click
browser.find_element_by_id('q').send_keys("some google search")
time.sleep(2)

browser.find_element_by_id('q').send_keys(Keys.ENTER)
time.sleep(2)


# 4. Close the browser
browser.close()
browser.quit()

