import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Background on user-agent

ua = UserAgent()

header ={'user-agent':ua.chrome}

page = requests.get("https://www.google.com",headers=header)
print(page.content)

# Background on Timeout
page = requests.get("https://www.google.com", timeout=3)

def read_file():
    file =open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data
# Make soup
# Syntax = BeautifulSoup(html_data,parser)
#Our parser is lmxl or html.parser which we have installed

html_file =read_file()
soup = BeautifulSoup(html_file, 'lmxl')# or for those who havent installed lxml -BeautifulSoup(html_file,'html.parser')

#soup_prettify
print(soup.prettify())

#identify some tags
