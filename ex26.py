def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #need to put : after defining a function
    """Prints the first word after popping it off."""
    word = words.pop(0) # Lol it's pop not poop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #close the brackets
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

six = 10 - 2 + 3 - 5
print "This should be six: %s" % six #numbers were giving 6 not 5

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # divide symbol was wrong
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)#shuld be _ not - also jelly was missing at the beginning

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (jelly_beans, jars, crates) #jelly was missing

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # There was typo and forgotten brackets


sentence = "All good\tthings come to those who wait."

words = break_words(sentence) #we didnt import ex25 so we are not going to use it
sorted_words = sort_words(words) #we didnt import ex25 so we are not going to use it

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #There was a dot in the beginning it shouldn't be there
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words #typo misplaced space

print_first_and_last(sentence) # typo f was missing

print_first_and_last_sorted(sentence) # typo t and nd was missing
