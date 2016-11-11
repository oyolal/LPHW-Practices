
states = {
    'Oregon'     : 'OR',
    'Ohio'       : 'OH',
    'California' : 'CA',
    'New York'   : 'NY',
    'Michigan'   : 'MI'
}

cities = {
    'CA': 'San Francisco',
    'OH': 'Cleveland',
    'FL': 'FT. Meyers',
    'MI': 'Ann Arbor'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print "-" * 20
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print "-" * 20
print "Ohio's abbr is: ", states['Ohio']
print "Michigan's abbr is: ", states['Michigan']

print "-" * 20
for state, abbr in states.items():
    print "%s is abbr'd %s." % (state, abbr)

print "-" * 20
for abbr, city in cities.items():
    print "%s has the city %s" % (abbr, city)

print "-" * 20
for state, abbr in states.items():
    print "%s is abbr'd %s and has the city %s." % (state, abbr, cities[abbr])

print "-" * 20
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

cities = cities.get('TX', 'Does Not Exist')
print "The city for 'TX' is: %s" % city
