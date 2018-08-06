# This is a modified webscraper that I found online for Craigslist data
# After the program scrapes the webpage it converets the list to a csv file


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

class CraiglistScraper(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.delay = 3

    def load_craigslist_url(self):

        #for i in range(2): #Number of pages that you want to scrape minus one Put the particular craigs list url you want to scrape
        self.driver.get(f"https://sfbay.craigslist.org/search/sss?search_distance=5&postal=94201&max_price=500")
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time")


    def extract_post_information(self):

        all_posts = self.driver.find_elements_by_class_name("result-row")

        dates = []
        titles = []
        prices = []


        for post in all_posts:

            title = post.text.split("$")

            if title[0] == '':
                title = title[1]
            else:
                title = title[0]
            title = title.split("\n")

            price = title[0]
            title = title[-1]

            title = title.split(" ")

            month = title[0]
            day = title[1]
            title = ' '.join(title[2:])
            date = month + " " + day
            #print("PRICE: " + price)
            #print("TITLE: " + title)
            #print("DATE: " + date+"\n")

            titles.append(title)

            prices.append(price)
            dates.append(date)
        return titles, prices, dates

    def extract_post_urls(self):
        url_list = []
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, "lxml")
        for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
            print(link["href"])
            url_list.append(link["href"])
        return url_list

    def quit(self):
        self.driver.close()


if __name__== "__main__":
    scraper = CraiglistScraper()
    scraper.load_craigslist_url()
    titles, prices, dates = scraper.extract_post_information()
    page_num = 1
    page_len = page_num * 120

    df =pd.DataFrame({'Count':range(page_len)})

    df['Titles'] = pd.Series(titles, index=df.index[:len(titles)])
    df['Price'] = pd.Series(prices, index=df.index[:len(prices)])
    df['Dates'] = pd.Series(dates, index=df.index[:len(dates)])

    df = pd.DataFrame(df)
    df.to_csv('CraigList_Scrape_2.csv',sep=',', header=['Count','Title','Price','Dates'], index=None)

    print("The File has been Read and csv has been created")

    scraper.quit()
