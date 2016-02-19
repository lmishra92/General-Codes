#Names, Variables, codes and function
#first define the function and then give the necessary commands
def cheese_and_cracker(cheese_count, boxes_of_crackers):
	print "You have %d cheese!"%cheese_count
	print "You have %d boxes of crackers"%boxes_of_crackers
	print "Get a plate.\n"
#giving the numbers directly
print "We can just give the function numbers directly:"
cheese_and_cracker(20,30)
#using variables from our script
print "Or we can use variables from our script"
cheese_count = 10
boxes_of_crackers = 50
cheese_and_cracker(cheese_count, boxes_of_crackers)
#maths inside the function
print "We can even do math inside too"
cheese_and_cracker(10+20, 50+60)
#combining variables and math
print "And we can combine variables and math:"
cheese_and_cracker(cheese_count+10, boxes_of_crackers+20)
