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


