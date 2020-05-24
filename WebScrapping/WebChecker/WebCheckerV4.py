#!/usr/bin/python3
import logging
import hashlib
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

logging.basicConfig(filename = 'WebCheckerV3.log',
                    level= logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s'
                    )

df = pd.DataFrame({
    'Date Modified':['5/17/2020', '5/17/2020','5/17/2020','5/17/2020','5/17/2020'],
    'URL':['https://www.destatis.de/EN/Themes/Economic-Sectors-Enterprises/Construction/Tables/permits.html', 'http://en.www.inegi.org.mx/app/tabulados/default.html?nc=807',
           'http://en.www.inegi.org.mx/app/tabulados/default.html?nc=448','http://en.www.inegi.org.mx/app/tabulados/default.html?nc=535',
           'http://en.www.inegi.org.mx/app/tabulados/default.aspx?nc=ca55_2018'],
    'HASH':['NA','NA','NA','NA','NA'],
    'Updated': ['N','N','N','N','N']
})
class Database():

    def __init__(self):
        self.dbLen = 4
        self.row = 0
        self.colUrl = 'URL'
        self.colHash = 'HASH'

    def urlGetter(self):
        url = df.loc[self.row, self.colUrl]
        return url

    def hashGetter(self):
        hash = df.loc[self.row, self.colHash]
        return hash

    def hashChanger(self, hash):
        hash = hash
        df.at[self.row, self.colHash] = hash

    def rowIncrementor(self):
        self.row += 1
        Database.dbChecker(self)

    def dbChecker(self):
        if self.row > self.dbLen:
            self.row = 0

class Checker:

    def __init__(self):
        self.dbLen = 4
        self.row = 0
        self.colUrl = 'URL'
        self.colHash = 'HASH'

    def hash(self, text):
        hashObj = hashlib.md5()
        hashObj.update(text.encode('utf-8'))
        hashed = hashObj.hexdigest()
        return hashed


    def parse(self, dirtyHtml):
        bs = BeautifulSoup(dirtyHtml, 'html.parser')
        table = bs.find(lambda tag: tag.name == 'table')
        tableRows = table.find_all('tr')
        tableArray = []
        for tr in tableRows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            tableArray.append(str(row)[1:-1])
            
        tableList = ''.join(tableArray)
        
        return tableList


    def dirtyHtml(slef, url):
        driver.get(url)
        sleep(5)
        sourceHtml = driver.page_source
        return sourceHtml

    def cleanHtml(self, sourceHtml):
        clean = self.parse(sourceHtml)
        print(clean)
        #logging.info('CleanHTML\n'.format(clean))
        return clean

    def handler(self, clean):

        if clean is None:
            logging.info('handler(output): No Table')

        else:
            encoded = self.hash(clean)
            return encoded

    def worker(self, url):
        dirty = self.dirtyHtml(url)
        clean = self.cleanHtml(dirty)
        hsh = self.handler(clean)

        #logging url
        logging.info('worker(url): {}'.format(url))

        return hsh

    def bot(self):
        url = Database.urlGetter(self)

        if Database.hashGetter(self) == 'NA':
            oldHash = self.worker(url)
            Database.hashChanger(self,oldHash)
            Database.rowIncrementor(self)

        else:
            newHash = self.worker(url)

            if Database.hashGetter(self) == newHash:

                logging.info('bot(output): Nothing new')
                Database.rowIncrementor(self)

            else:
                logging.info('bot(output): Something new')
                Database.hashChanger(self, newHash)
                Database.rowIncrementor(self)
            #sleep(10)

if __name__ == '__main__':
    c = Checker()
    while True:
        c.bot()
