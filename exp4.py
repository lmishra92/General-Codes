from sys import argv

dating_website, user_name = argv

print "Hello %s. Welcome to the %s"% (user_name, dating_website)
print "Before we begin, I would like to ask you some questions about you. Is that okay ?"
print "Where do you live ?"
live = raw_input()

print "What is your qualification ?"
qualification = raw_input()

print "What kind of girl are you looking for ?"
girl = raw_input()

print """ Thank you for cooperating. You are
from %r, your qualification is %r and you are looking for a %r girl"""% (live, qualification, girl)
