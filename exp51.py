print "please enter the file you want to open"
file_name = raw_input()
text = open(file_name)
print text.read()
