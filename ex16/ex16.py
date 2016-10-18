from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#Getting user approval
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#Here we are erasing the file
print "Turncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#Here we are getting new text for the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#Writing down those texts we took from user
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
