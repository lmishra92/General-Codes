#function practice
def details(name, age, weight, university):
	print "Your name is %s"% name
	print "Your age is %d"% age
	print "Your weight is %d kilos"% weight
	print "You are in %s university"% university
	
#assign values directly
print "Now I am assigning values directly"
details("Lenin Mishra", 23, 85, "TU Delft")

#use variables to assign values
print "Now I am assigning values through variables in my script" 
name = "Lenin Mishra"
age = 23
weight = 85
university = "TU Delft"
details(name, age, weight, university)

#putting maths inside
print "Now I am trying to put maths inside"
details("Lenin Mishra", 20+3, 17*5, "TU Delft")

#combining variables and maths
print "Now I am combining variables and maths"
age= 20
weight= 85
details("Lenin Mishra", age+10, weight+20, "TU Delft")
