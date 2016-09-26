tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
### Instead of """ you can also use '''
### It is just based on style
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print "%s" % tabby_cat  # %s lets you edit the string the way you want
print "%r" % persian_cat# %r is just a raw printing
print backslash_cat
print fat_cat

### Here is the funny code that prints loading screen

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i
