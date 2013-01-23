print "For Loop......."
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

elements = []

for i in range(0, 6):
    elements.append(i)
for i in elements:
    print "Element was: %d" % i

print "While Loop....."

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
print "The numbers: "

for num in numbers:
    print num
