#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple script that shows how beautiful soup is used
"""

# 1. Import some useful libraries
import requests
from bs4 import BeautifulSoup

# 2. Get the website data

# use requests to get the website
result = requests.get("http://www.apostolos-filippas.com/")

# store the webpage content to a variable
src = result.content

# 3. Use BS to parse and process

# first create a BS object
soup = BeautifulSoup(src)

# 3.1.1 find all links contained in the page
links = soup.find_all("a")

# 3.1.2 you cab also print specific attributes of each link
for link in links:
    print(link.attrs['href'])
    
# 3.1.3 finding all of my paper titles is now easy!
for link in links:
    if "papers" in link.attrs['href']:
        # of course, you have to find the correct BS method
        print(link.string)
        
        
''' Notes

    To print a prettier soup, use print(soup.prettify())
    The outcome may be easier for you to parse!
    
    BS has a lot of other useful features. In the optional readings, 
    I link to a tutorial that will allow you to further your BS knowledge

'''