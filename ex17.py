from sys import argv
from os.path import exists

#We'll copy contents of one file to another
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

#How could we do these on one line?
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

#Exists returns True or False depending on if file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#You don't need to close indata because when you open.read() python
#automatically closes it for you
