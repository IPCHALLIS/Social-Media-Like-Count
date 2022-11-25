"""
This program implements a function which takes an array of people's names who like an item on Facebook.
The function should create some text to be displayed next to such an item.
For 4 or more names, the number in "and 2 others" simply increases.
"""

ending1 = ('likes this') # sentence ending for a single like
ending2 = ('like this') # sentence ending for two-to-three likes
connect = ('and') # connecting word for multiple likers
ending3 = ('others like this') # sentence ending for more than three likes

def likes(names):
    names = list(names) # assign names variable to list
    if len(names) == 0: # if list is empty
        return "no one likes this" # return no likes
    elif len(names) == 1: # if list has only one name
        return "{} {}".format(','.join(names), ending1)
    elif len(names) == 2: # if list has two names
        return "{} {}".format(' and '.join(names), ending2)
    elif len(names) == 3: # if list has three names
        return "{} {} {} {}".format(', '.join(names[0:2]), connect, ','.join(names[2:3]), ending2)
    elif len(names) > 3: # if list has more than three names
        return "{} {} {} {}".format(', '.join(names[0:2]), connect, len(names)-2, ending3)

print(likes([])) # should print "no one likes this"
print(likes(['Peter'])) # should print "Peter likes this"
print(likes(['Jacob', 'Alex'])) # should print "Jacob and Alex like this"
print(likes(['Max', 'John', 'Mark'])) # should print "Max, John and Mark like this"
print(likes(['Alex', 'Jacob', 'Mark', 'Max'])) # should print "Alex, Jacob and 2 others like this"