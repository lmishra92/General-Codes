import re
import urllib
import xml.etree.ElementTree as ET
sum = 0
list = []
#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url = raw_input('Enter location: ')
#url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
#print tree
results = tree.findall('.//count')
#print results
print "Counts", len(results)
noteinfo = tree.findall('comments/comment')
for item in noteinfo:
	numbers = item.find('count').text
	numbers = numbers.split()
	for number in numbers:
		i = float(number)
		sum = sum + i
print sum
	


		


	
	
	
