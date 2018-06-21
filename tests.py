import main

url = "https://www.ynet.co.il/home/0,7340,L-4269-32-187-201701-1,00.html"
soup = main.get_soup(url)
print(soup.find('body').findChildren())