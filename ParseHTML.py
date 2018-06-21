properties
topic
tables = document.getElementsByClassName("classMainTableBox")
for table in tables:
	for link in table.getElementsByTagName("a"):
		if(link.innerHTML == properties["topic"]):
			# go to link.href

table = document.getElementsByClassName("classMainTable")[0]
years = table.getElementsByClassName("classMainTitle")
for year in years:
	if year.children[0].innerHTML.find(properties["year"]) != -1:
		

