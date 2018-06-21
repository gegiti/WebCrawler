import requests
from bs4 import BeautifulSoup
from ParseHTML import *

def get_properties():
    properties = dict()
    properties["topic"] = "כדורגל עולמי";
    properties["year"] = "2005"
    properties["month"] = "מרץ"
    return properties
    properties = dict()
    properties["topic"] = raw_input("What topic? ")
    properties["year"] = raw_input("What year? ")
    properties["month"] = raw_input("What month? ")
    return properties

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def getArticleText(page):


if __name__ == '__main__':
    print(get_soup(getArticleText("https://www.ynet.co.il/articles/0,7340,L-5079179,00.html")))
    addr = "https://www.ynet.co.il/home/0,7340,L-4269,00.html"
    soup = get_soup(addr)
    properties = get_properties()
    addr = "https://www.ynet.co.il" + getTopicURL(soup, properties)
    print("Topic URL: "+addr)
    soup = get_soup(addr)
    addr = "https://www.ynet.co.il" + getArticlesURL(soup, properties)
    print("Articles URL: "+addr)

