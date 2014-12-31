from sys import argv

script, input_file = argv

#This is doing to print the contents of a file object that gets passed to it
def print_all(f):
    print f.read()

# Seek - postion (think text cursor) of where python is in the file.
#   (offset, from_where)
# offset is how much you want to adjust
# from_where - 0 is beginning, 1 is current location, 2 is end
def rewind(f):
    #By putting it at 0 that simply means to start at the beginning again
    f.seek(0)

# Only reads one line of the file
def print_a_line(line_count, f):
    print line_count, f.readline()


# Opens the file given upon start
current_file = open(input_file)
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
