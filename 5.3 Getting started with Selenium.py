"""
This script gets you ready to use Selenium.
    To be able to use Selenium, you first have to get the correct browser driver
    Go to https://www.seleniumhq.org/download/ and download your preferred one
    I downloaded Chrome, and will be using this one for the rest of this class
    
    If you have any problem during the installation, please email the TA
"""

from selenium import webdriver

# Now open an instance of the Chrome browser.
# The instance of Chrome that opened will indicate that  
# "Chromes is now being controlled by automated test software" on the upper left corner
# Note: you have to define the path where you saved your driver!
browser = webdriver.Chrome("/Users/apostolosfilippas/misc/chromedriver" )

# visit a website
browser.get("http://www.apostolos-filippas.com/")

# close the browser
browser.quit()

# That's it! You're ready for the next lecture :)