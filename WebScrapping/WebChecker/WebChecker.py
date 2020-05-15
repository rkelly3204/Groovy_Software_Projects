import hashlib
import requests
import pandas as pd
from tabulate import tabulate
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

def Hsh(txt):
    a = hashlib.md5()
    a.update(txt.encode('utf-8'))
    hshd = a.hexdigest()
    return hshd

def Parser(dirtyHtml):
    bs = BeautifulSoup(dirtyHtml, 'html.parser')
    table = bs.find(lambda tag: tag.name == 'table')
    return table

def DirtyHTML(url):
    driver.get(url)
    htmlSource = driver.page_source
    return htmlSource

def CleanHTML(htmlSource):
    cleanHtml = Parser(htmlSource)
    return cleanHtml

def Handler(cleanHtml):
    if cleanHtml is None:
        print("No Table")
    else:
        encoded = Hsh(cleanHtml)
        return encoded
def  custom (dirtyHtml):
    soup = BeautifulSoup(dirtyHtml, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    print(tabulate(df[0], headers='keys', tablefmt='psql'))

def bot(id,url):

    id = id
    dirtyHtml = DirtyHTML(url)
    cleanHtml = CleanHTML(dirtyHtml)
    prevHash = Handler(cleanHtml)

    while True:
        newHash = Handler(cleanHtml)
        if prevHash == newHash:
            print("Nothing new")
            custom(dirtyHtml)
        else:
            print("New stuff posted")
            prevHash = newHash

        sleep(90)

if __name__ == '__main__':
    url = 'https://www.nationmaster.com/country-info/stats/Media/Internet-users'
    id = "IHUN.2121"

    r = requests.get(url)
    if r.status_code == 404:
        print("Website is not valid: "+url)
        print("Change link for: "+id)
    else:
        bot(id,url)
