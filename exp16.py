#Branches and function

from sys import exit

def gold_room():
	print "You are in a room full of gold"
	print "How much do you want ?"
	choice = int(raw_input(">"))
	
	if choice < 50:
		print "You are not greedy. You can take the gold."
		exit()
	elif choice >50 and choice <100:
		print "Penalty. You are greedy. Go back to the dark room."
		start()
	elif choice > 100:
		dead()
	else:
		print "Learn to choose"
		gold_room()
	
	
def start():
	print "You are in a dark room."
	print "There are two doors, one to your left and one to your right"
	print "Which one do you take ?"
	choice = raw_input (">")
	if choice == "left":
		lion_room()
	elif choice == "right":
		snake_room()
	else:
		dead("You die doing nothing")
		
def dead():
	print "You are dead. Hard luck"
	exit(0)
	
def lion_room():
	print "You are in a lion room"
	print "He is standing in front of a door"
	print "You can either taunt him, ask him nicely or do a trick to go into that room"
	print "What would you do ?"
	
	choice = raw_input(">")
	
	if choice == "taunt" or choice == "ask":
		dead()
	elif choice == "trick":
		print "Congrats..you are going into the gold room !"
		gold_room()
	else:
		print "You will die anyway. Its better you make a choice"
		lion_room()
		
def snake_room():
	print "You are int he snake room"
	print "He is drinking milk"
	print "He is infront of a door"
	print "You can either take away milk, attack the snake or sing a song"
	print "What will you do ?"
	
	choice = raw_input(">")
	if choice == "take" or choice == "attack":
		dead()
	elif choice == "sing":
		print "The snake slept. You can pass the door"
		gold_room()
	else:
		print "You will die anyway. Better make a choice !"
		snake_room()
		
start()
