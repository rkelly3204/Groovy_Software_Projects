import pandas as pd
import re
import time
import bs4
import requests

links=[]
pages = set()
def getLinks(pageUrl):
    global pages

    print(pageUrl)
    res = requests.get(pageUrl)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for link in soup.findAll('a',href = True):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                #print("https://www.opendataphilly.org"+newPage)
                links.append(str("https://www.opendataphilly.org/dataset/fatal-crashes" + link.attrs['href']))
                pages.add(newPage)
                if "http" not in newPage:
                    getLinks("https://www.opendataphilly.org/dataset/fatal-crashes"+newPage)
                else:
                    getLinks(newPage)
                    #links.append(str("https://www.opendataphilly.org"+link.attrs['href']))

    print("Done at Links")
    return links

def getCSV(Url):
    for i in getLinks(Url):
        time.sleep(.25)
        if "groups" not in i:
            res = requests.get(str(i))
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            for link in soup.find_all('a',attrs={'href': re.compile(".csv")}):
                csvname(link['href'])

                print("Done at csv")
                return link['href']

def csvname(name):
    name.strip('/')
    name.strip('.')

    print("Done at name")
    return name

def downloadCSV(URL):
    df = pd.read_csv(getCSV(URL))
    df.to_csv(csvname()+'.csv')

    print("Done at Download")

downloadCSV('https://www.opendataphilly.org/dataset/fatal-crashes')
