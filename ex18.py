#THis one is like scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# - *args is useless, passing arguments is the same as unpacking them:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nothin."


print_two("Courtney", "Peters")
print_two_again("Courtney", "Peters")
print_one("First!")
print_none()
