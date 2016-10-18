def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can use varibles from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)



print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, varibles and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#My own function
def print_something():
    print "Something\n"
    print "Lol\n"
    print "Kiddin\n"
    print "Enter the amount of cheeses and crackers:\n"
    x = raw_input("cheeses: ")
    y = raw_input("crackers: ")
    z = (int(x) + int(y))/10
    print "So according to my calculations %r amount of cheeses and %r amount of crackers will last %2.f hours" % (x ,y ,z)


print_something()
