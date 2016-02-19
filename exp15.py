#loops and lists


def loop(i, num):
	number = 0
	while number < i:
		print "the number is %d"%number
		num.append(number)
		number +=1
		if number == i:
			print "Invalid"
		

	
	
	
a =int(raw_input(">"))
num = []
loop(a, num)

for numbers in num:
	print numbers