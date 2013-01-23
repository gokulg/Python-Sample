print "Hello World."
print 'I "really" love this.'

print "3+2 = ", 3+2
print "Is it greater?", 5 > -2
print 31 + 122 + 15 - 425 + 4 % 24 - 1 / 45 + 61


cars = 100
drivers = 30
cars_driven = drivers
passengers = 90
average_passengers_per_car = passengers / cars_driven
print "There needs to be about an average of", average_passengers_per_car, "in each car."


name = 'Gokul'
age = 23
height = 174
weight = 90
print "He is %d pounds heavy." %weight
print "If I add my %d, %d, and %d I would get %d." %(age, height, weight, age + height + weight)

role = "Developer"
print "I am a %s" %role

opinion = False
joke = "Is that joke is so funny?! %r"
print joke %opinion

w = "Could you please "
e = "get me to the other side?"
print w + e

print "Her hair is %s as snow." %'white'
print "Gokul " *5

days = "\nMon\nTue\nWed\nThu\nFri\nSat\nSun"
print "A week consist of: ", days

print "How much do you weigh?",
weight = raw_input()
age = raw_input("How old are you? ")
print "Age = %r Weight = %r." %(age, weight)
