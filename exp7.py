from sys import argv
from os.path import exists

script, from_file, to_file = argv

infile = open(from_file)


print "Copy will happen from %s to %s"% (from_file, to_file)
print "The size of the file is %d"% len(infile.read())
print "Does the output file exists ? %r"% exists(to_file)
print "IF you want to continue copying, press enter or else ctrl c"
raw_input("?")

copyfile = open(to_file, 'w')
copydata = copyfile.write(infile.read())


print "Copying finished"

infile.close()
copyfile.close()






