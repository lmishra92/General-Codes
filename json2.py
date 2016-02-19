import urllib
import json
sum = 0
input = raw_input(">")
uh = urllib.urlopen(input)
data = uh.read()
print "Retrieved", len(data), "characters"
info = json.loads(data)
print 'User count:', len(info)
usedata = info["comments"]
print usedata
for item in usedata:
	x = item["count"]
	sum = sum + x 
print sum

	

    

