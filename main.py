import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    addr = "https://www.ynet.co.il/home/0,7340,L-8,00.html"
    page = requests.get(addr)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title)