#Reading files

from sys import argv
script, file_name = argv #Using argv to get a file name
text = open(file_name) #opens the required file
print "Here is your file, %r"%file_name
print text.read() #Remember, to read the file..you have to first open the file.

print "Open another file."
file2 = raw_input() #using raw input and argv together
text2 = open(file2)
print text2.read() # we give command to a file by using the 'dot' operator
