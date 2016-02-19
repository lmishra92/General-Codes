import re
import urllib
from BeautifulSoup import *
list = []
def parsing(i, url, position):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	for tag in tags:
		links = tag.get('href', None)
		list.append(links)
	url1 = list[position]
	print url1
	return list
	while i<count:
		parsing(i, url1, position)
		i+=1
	

	
i=0
url = raw_input("URL>")
count = int(raw_input("count>"))
position = int(raw_input("position>"))
parsing(i, url, position)
