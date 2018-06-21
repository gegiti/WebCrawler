def getTopicURL(page, properties):
	tables = page(class_="classMainTableBox")
	for table in tables:
		for link in table("a"):
			if(link.get_text() == properties["topic"]):
				return link.get('href')

def getArticlesURL(page, properties)
	years = page(class_="classMainTable")[0](class_="classMainTitle")
	for year in years:
		if years[0].get_text().find("2017") != -1:
			for month in year.parent("td"):
				if(month.get_text().find(properties["month"]) != -1):
					return month("a")[0].get('href')


