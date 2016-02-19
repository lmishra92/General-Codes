def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == 'rock':
        value = 0
    elif name == 'spock':
        value = 1
    elif name == 'paper':
        value = 2
    elif name == 'lizard':
        value = 3
    elif name == 'scissors':
        value = 4
    else:
        print "Invalid name!"
    return value

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
		name = 'rock'
	elif number == 1:
		name = 'spock'
	elif number == 2:
		name = 'paper'
	elif number == 3:
		name = 'lizard'
	elif number == 4:
		name == 'scissors'
	else:
		print "Invalid number"
    return name
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print "============"
    # print out the message for the player's choice
    print "I choose", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
	comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
	print "Computer choice is", comp_choice
    # compute difference of comp_number and player_number modulo five
	dif = comp_number - player_number
    # use if/elif/else to determine winner, print winner message
	if dif <= 2:
		print "Computer wins"
	elif dif >2:
		print "I win"
	elif dif < 0 and dif >= -2:
		print "I win"
	elif dif < -2:
		print "Computer Wins"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


