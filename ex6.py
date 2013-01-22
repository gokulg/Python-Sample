def details(name, age):
    print "My name is %s" % name
    print "Age is %d" %age

print "We can just give the function numbers directly:"
details("Gokul", 23)


print "OR, we can use variables from our script:"
my_name = "Gokul G"
my_age = 25
details(my_name, my_age)


print "We can even do math inside too:"
details("Gokul" + "G", 23 + 5)
