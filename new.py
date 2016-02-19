import random
print "Choose between rock, paper and scissor"
user = raw_input("Choice >")
comp = random.choice(['rock', 'paper', 'scissor'])

print "You chose", user
print "The comp chose", comp

if comp == 'rock':
	if user == 'rock':
		print "Tie"
	elif user == 'paper':
		print "You win"
	else:
		print "Computer wins"
		
elif comp == 'paper':
	if user == 'rock':
		print "Computer wins"
	elif user == 'paper':
		print "Tie"
	else:
		print "You win"
		
elif comp == 'scissor':
	if user == 'rock':
		print "You win"
	elif user == 'paper':
		print "Computer wins"
	else:
		print "Tie"
		
while True:
	print "The game is still running"
	input = raw_input("Want to play again >")
	if input == 'n':
		break
	else:
		continue