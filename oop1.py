class Partyanimal:
	x = 0
	name = ""
	def __init__(self, nam):
		self.name = nam
		print self.name,"constructed"
		
	def party(self):
		self.x+=1
		print self.name,"party count", self.x
		
	def __del__(self):
		print "I am destroyed", self.x
		
		
an = Partyanimal("Lenin")
an.party()

ban = Partyanimal("Mishra")
ban.party()
ban.party()
an.party()