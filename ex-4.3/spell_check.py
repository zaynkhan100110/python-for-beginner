



 # this file contains how to check word spells with .startwith() functions

"become".startswith("be")  # This will not going to print anything in normal terminal you may need python shell



print ('') # just a new line blank space
print ("This checks from front of the words")  # explaination
print ('')
string1 = "Becomes"  # just a string with value assign to a variable
string1.startswith("be")  # this checks and prints is if the string value starts with ( be ) or not (this will work only on python shell not on normal terminal

print (string1.startswith("be"))   # just print


string2 = "becomes"  # just a string with value assign to the variable
print (string2.startswith("be"))  # this checks and prints is if the string value starts with ( be ) or not ( since we use print() function so this will be print on any terminal 

string3 = "BEAR"  # just a string with value assign to the variable
print (string3.startswith("be"))   # just print

string4 = " beautiful"  # just a string with value assign to the variable
print (string4.startswith("be"))  # just print


print ('')

print ('This checks from back of the word')
print ("")

string1 = "Becomes"  # just a string with value assign to a variable
string1.endswith("be")  # this checks and prints is if the string value starts with ( be ) or not (this will work only on python shell not on normal termi>

print (string1.endswith("be"))   # just print


string2 = "becomes"  # just a string with value assign to the variable
print (string2.endswith("be"))  # this checks and prints is if the string value starts with ( be ) or not ( since we use print() function so this will be >

string3 = "BEAR"  # just a string with value assign to the variable
print (string3.endswith("be"))   # just print

string4 = " beautiful"  # just a string with value assign to the variable
print (string4.endswith("be"))  # just print

