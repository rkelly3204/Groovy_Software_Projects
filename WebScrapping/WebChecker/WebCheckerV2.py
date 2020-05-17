#!/usr/bin/env python3
import logging
import hashlib
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

logging.basicConfig(filename = 'WebCheckerV2.log',
                    level= logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s'
                    )

class Checker:

    def hash(self, text):
        hashObj = hashlib.md5()
        hashObj.update(text.encode('utf-8'))
        hashed = hashObj.hexdigest()
        return hashed

    def parse(self, dirtyHtml):
        bs = BeautifulSoup(dirtyHtml, 'html.parser')
        table = bs.find(lambda tag: tag.name == 'table')
        return table

    def dirtyHtml(slef, url):

        driver.get(url)
        sourceHtml = driver.page_source

        return sourceHtml

    def cleanHtml(self,sourceHtml):
        clean = self.parse(sourceHtml)
        return clean

    def handler(self, clean):

        if clean is None:
            output = "No table"
            logging.info('handler(output): {}'.format(output))
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

    def bot(self, url):
        oldHash = self.worker(url)

        while True:
            newHash = self.worker(url)

            if oldHash == newHash:
                botOutput = "Nothing new"
                logging.info('bot(output): {}'.format(botOutput))

            else:
                botOutput = "Something new"
                logging.info('bot(output): {}'.format(botOutput))
                oldHash = newHash

            sleep(10)


if __name__ == '__main__':
    url = 'https://www.nationmaster.com/country-info/stats/Media/Internet-users'
    c = Checker()
    c.bot(url)
