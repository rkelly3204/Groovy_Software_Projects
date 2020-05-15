from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver

# launch url
search = ["QUARTERBACK"]
        #for i in range(2): #Number of pages that you want to scrape minus one Put the particular craigs list url you want to scrape
for i in search:
    url = f'http://www.nfl.com/stats/categorystats?tabSeq=1&season=2018&seasonType=PRE&d-447263-p=1&statisticPositionCategory={i}&qualified=true'

# create a new Chrome session
    driver = webdriver.Chrome()

# go to url
    driver.get(url)

# Selenium hands the page source to Beautiful Soup
    soup = bs(driver.page_source,"lxml")
    info_list = []
    b = driver.find_element_by_id('result')
    c = b.text
    lines = c.split('\n')
    #print(f"{lines}")
    csvList = []
    for j in lines:
        splitLine = j.split()
        print(splitLine)
        csvLine = ""
        for k in splitLine:
            csvLine = csvLine + k + ","
        print(csvLine)
        csvList.append(csvLine)

    with open('QUARTERBACK_2018_pre.csv','w') as file:
        for l in csvList:
            file.write(l)
            file.write('\n')
driver.close()
