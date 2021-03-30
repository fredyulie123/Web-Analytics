"""
This script scrapes two pages of tweets
"""

# 1. import useful libraries
from selenium import webdriver
import time

# 2.1 Open an instance of the Chrome browser
browser = webdriver.Chrome("/Users/apostolosfilippas/misc/chromedriver" )

# 2.2 set implicit wait to 10 seconds
browser.implicitly_wait(10)

# 3. Scrape tweets

# 3.1 Provide url
url='https://twitter.com/SHAQ'

# 3.2 Visit the link
browser.get(url)
time.sleep(5)

# 3.3 Scroll down twice to load more tweets
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# 3.4 Find all elements with a class that ends in 'tweet-text'
tweets = browser.find_elements_by_css_selector("[class*=original-tweet]")

# 3.5 Write the tweets to a file
with open('files/tweets.txt','w',encoding='utf8') as fw:
    for tweet in tweets:
        
        txt,retweets='NA','NA'
        
        try: 
            txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
        except: 
            print ('no text')     
    
        try:
            retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
            retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
        except:
            print ('no retweets')
    
        fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\n')

# 4. close browser
browser.close()        
browser.quit()
