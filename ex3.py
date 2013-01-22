from sys import argv

script, name = argv
prompt = '> '

print "Hi my name is %s" % (name)
print "Where do you live?"
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
You live in %r.
And you have a %r computer.
""" % (lives, computer)

