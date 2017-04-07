from __future__ import division                             # this lets you divide numbers and get floating results
import math                                                 # this lets you do math
import re                                                   # this lets you make string replacements: 'hi there'.replace(' there') --> 'hi'
import os                                                   # this lets you set system directories
import time                                                 # this lets you slow down your scraper so you don't crash the website =/
import codecs                                               # symbols are annoying. this lets you replace them.
import random                                               # this lets you draw random numbers.
import datetime                                             # this lets you create a list of dates
from datetime import timedelta                              # same
from selenium import webdriver                             # the rest of these let you create your scraper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities.FIREFOX
caps['marionette'] = True
caps['binary'] = '/Applications/Firefox.app/Contents/MacOS/firefox-bin'
chromedriver = "/Users/T/Google Drive/Lab on Non-Democratic Politics/Scraping/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# set your working directory
writedir = '/Users/T/Google Drive/Lab on Non-Democratic Politics/Scraping'

# set your writepath
f = open(writedir+'test.txt','a')

# set the dates you want to scrape
# date format: YYYY-D-MM
startdate = '2017-3-20'
enddate = '2017-3-20'

PAGERESULTS = 'pagination_hldr'

f = open(writedir+'MENA.txt','a')
date = datetime.datetime.strptime(startdate, "%Y-%m-%d")
while date <= datetime.datetime.strptime(enddate, "%Y-%m-%d"):
    print startdate
    # nav to URL
    n = 1 # for now, go to the first result page
    url = 'https://www.mena.org.eg/en/search/index/table/Search+Text+News/from_date/'+startdate+'/to_date/'+enddate+'/search/Search+Text+News/page/'+str(n)
    print 'getting URL:',url
    driver.get(url)
    time.sleep(1)
    # find # of results
    rdiv = driver.find_element_by_id(PAGERESULTS)
    results = rdiv.text
    results = results.strip()
    results = results.strip("<,Previous, Next, >, |")
    results = results.split() # turning pageresults into list
    resultPages = results[-1] # taking last page number of list as total page number
    print 'Result pages:', resultPages
    # get the text from each of those result pages
    for page in range(1,int(resultPages)+1):
        print 'page ' + str(page) + ' of ' + str(int(resultPages))
        time.sleep(random.uniform(5,10))
        div = driver.find_element_by_id('advancedsearchResults')
        time.sleep(random.uniform(1,2))
        text = div.text
        text = text.encode('utf-8')
        # print text[0:100]
        f.write(text+'\n\n******************\n\n')
        n += 1
        suburl = 'https://www.mena.org.eg/en/search/index/table/Search+Text+News/from_date/'+startdate+'/to_date/'+enddate+'/search/Search+Text+News/page/'+str(n)
        print 'pass'
        time.sleep(1)
        driver.get(suburl)
    date += timedelta(days=1)

f.close()
