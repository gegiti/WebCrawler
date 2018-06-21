def getTopicURL(page, properties):
	tables = page(class_="classMainTableBox")
	for table in tables:
		for link in table("a"):
			if(link.get_text() == properties["topic"]):
				return link.get('href')

def getArticlesURL(page, properties):
	years = page(class_="classMainTable")[0](class_="classMainTitle")
	print("goin over years...")
	for year in years:
		print(year.get_text())
		if year.get_text().find(properties["year"]) != -1:
			print("goin over months...")
			for month in year.parent("td"):
				print(month.get_text())
				if(month.get_text().find(properties["month"]) != -1):
					return month("a")[0].get('href')

def getArticleText(page):
    article = page("block B3")[0]
    articleBody = page("art_body_width_3")[0]
    txt = articleBody.get_text()

def working():
	print(get_soup(getArticleText("https://www.ynet.co.il/articles/0,7340,L-5079179,00.html")))
    addr = "https://www.ynet.co.il/home/0,7340,L-4269,00.html"
    soup = get_soup(addr)
    properties = get_properties()
    addr = "https://www.ynet.co.il" + getTopicURL(soup, properties)
    print("Topic URL: "+addr)
    soup = get_soup(addr)
    addr = "https://www.ynet.co.il" + getArticlesURL(soup, properties)
    print("Articles URL: "+addr)