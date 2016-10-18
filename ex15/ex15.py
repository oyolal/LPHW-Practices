from sys import argv

script, filename = argv
# opening the file for editing
txt = open(filename)

print "Here's your file %r:" % filename
#printing text from that file
print txt.read()

print "Type the filename again:"
#getting file name from user
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
