class Set:
	def __init__(self):
		"""Initialize a dictionary"""
		self.data = {}
		
	def contains(self, element):
		"""Checks whether self.data dict has element as it's key"""
		return self.data.has_key(element)
	
	def add(self, element):
		self.data[element] = 1
	def elements(self):
		"""Returns a list of all the available keys in the self.data dict"""
		keys = self.data.keys()
		keys.sort()
		return keys
		
class Numdict:
	"""Dictionary to categorize numbers"""
	def __init__(self, input = None):
		self.data = {}
		if input is not None:
			for item in input:
				(category, value) = item
				self.inc(category, value)
				
	def __getitem__(self, key):
		"""get function returns a value for the key or else will return 0"""
		return self.data.get(key,0)
		
	def __setitem__(self, key, value):
		self.data[key] = value
		
	def inc(self, key, value):
		"""Updating a value of a key"""
		self.data[key] = self.data.get(key,0) + value
		
	def items(self):
		it = self.data.items()
		it.sort()
		return it
		
	def clear(self):
		"""Removes all the elements of dictionary"""
		self.data.clear()
		
		
myset = Set()
myset.add('Spam')
myset.add('Eggs')
myset.add('Spam')
print myset.contains('beer')
print myset.elements()