from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def single_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "The whole file:\n"

print_all(current_file)

print "Rewind"

rewind(current_file)

print "Let's print three lines:"

current_line = 1
single_line(current_line, current_file)

current_line = current_line + 1
single_line(current_line, current_file)

current_line = current_line + 1
single_line(current_line, current_file)


def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

result = add(5,7)
print "Added Result: %d" %result

