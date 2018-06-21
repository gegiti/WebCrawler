import requests
from bs4 import BeautifulSoup


def get_properties():
    properties = dict()
    properties["topic"] = raw_input("What topic? ")
    properties["year"] = raw_input("What year? ")
    properties["month"] = raw_input("What month? ")
    return properties

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


if __name__ == '__main__':
    addr = "https://www.ynet.co.il/home/0,7340,L-4269,00.html"
    soup = get_soup(addr)
    properties = get_properties()

