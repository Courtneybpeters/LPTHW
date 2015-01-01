#ARGV is within sys
from sys import argv

#Remember argv asks for variables when your program starts
#There's script first because when you type in the terminal:
# python ex15.py stuffyoutype
#the name of the script is an argument you have passed it so you only use the
#second argument really
script, filename = argv

#This creates a file OBJECT
txt = open(filename)

print "Here's your file %r:" % filename

#Reads through the data stored in txt
print txt.read()

#This tells the user, then prompts them, for the same file name but again.
print "Type the filename again:"
file_again = raw_input("> ")

#This opens the file and gets the data from it
txt_again = open(file_again)

#This reads the file
print txt_again.read()


#Additional - close text files
txt.close()
txt_again.close()


#You can open a file more than once, as evidenced by this exercise
