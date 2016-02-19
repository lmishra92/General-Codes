# using return function
def add(a,b):
	print "Adding %d + %d"%(a,b)
	return a + b

def subtract(a,b):
	print "Subtracting %d - %d"%(a,b)
	return a - b 
	
def multiply(a,b):
	print "Multiplying %d * %d"%(a,b)
	return a * b
	
def divide(a,b):
	print "dividing %d / %d"%(a,b)
	return a / b
	
print "Let us do some math"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age:%d, Height:%d, Weight:%d, iq:%d"%(age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print "That becomes:", what, "can you do it by hand ?"

print 7/4

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r"%i