from sys import argv
script = argv

print "We are going to erase the contents of a file today"
print "Give a file to delete"
file_name = raw_input()

print "Are you sure to delete it ?"
print "Press ctrl-C (^C) to change your opinion"
print "If you still want the same, press return"
raw_input("?")

target = open(file_name, 'w')
target.truncate()

print "Now add three lines."

line1 = raw_input('>')
line2 = raw_input('>')
line3 = raw_input('>')
#target.write(line1, "\n", line2, "\n", line3, "\n")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally we close it."
target.close()
