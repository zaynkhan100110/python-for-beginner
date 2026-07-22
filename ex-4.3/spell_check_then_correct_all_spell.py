



# this file contains how to replace and correct all the strings and make them all true




print (' ')

 # this file contains how to check word spells with .startwith() functions

"become".startswith("be")  # This will not going to print anything in normal terminal you may need python shell



print ('') # just a new line blank space
print ("This checks from front of the words")  # explaination
print ('')
string1_1 = "Becomes"  # just a string with value assign to a variable
string1_1_1 = "be" + string1_1[1:]
string1_1_1.startswith("be")  # this checks and prints is if the string value starts with ( be ) or not (this will work only on python shell not on normal termi>

print (string1_1_1.startswith("be"))   # just print

print (string1_1_1)


string2_2 = "becomes"  # just a string with value assign to the variable
string2_2_2 = "be" + string2_2[1:]
print (string2_2_2.startswith("be"))  # this checks and prints is if the string value starts with ( be ) or not ( since we use print() function so this will be >
print (string2_2_2)


string3_3 = "BEAR"  # just a string with value assign to the variable
string3_3_3 = 'be' + string3_3[2:]
print (string3_3_3.startswith("be"))   # just print
print (string3_3_3)



string4_4 = " beautiful"  # just a string with value assign to the variable
string4_4_4 = "be" + string4_4[2:]
print (string4_4_4.startswith("be"))  # just print
print (string4_4_4)


print ('')

print ('This checks from back of the word')
print ("")

# trick is just swap the position since you swap the order

strings1 = "Becomes"  # just a string with value assign to a variable
strings1_1 = strings1[2:] + "be"  # this cuts from left side and preserve everything  on right side
strings1_1.endswith("be")  # this checks and prints is if the string value starts with ( be ) or not (this will work only on python shell not on normal termi>

print (strings1_1.endswith("be"))   # just print
print (strings1_1)

strings2 = "becomes"  # just a string with value assign to the variable
strings2_2 = strings2[:-2] + 'be'  # in this slice this just cut 2 words (since i put 2 in slice) and preserve everything left on right side
print (strings2_2.endswith("be"))  # this checks and prints is if the string value starts with ( be ) or not ( since we use print() function so this will be >
print (strings2_2)

strings3 = "BEAR"  # just a string with value assign to the variable
strings3_3 = strings3[:2] + 'be'  # in this slice [:2] it cuts everything from right side and just preserve the ledt side words amount you enter in the slice which is 2
print (strings3_3.endswith("be"))   # just print
print (strings3_3)

strings4= " beautiful".lstrip()  # just a string with value assign to the variable
strings4_4= strings4[:-2] + "be"  # here it will just cut last 2 words (we put slice value of 2) and preseve everything on left side
print (strings4_4.endswith("be"))  # just print
print (strings4_4)





# what the slice exactly how this works ?

# slice is simple if you can get the methology

# frist you want add words infront of existed word (i.e. "word" i want to cut the "wo" then slice like this [2:] and for from back side like this [:-2]



## in simplw words if you want to preserve left side and cut right side then use [:-amount] and if you want to preserve right side and cut left side then use [amount:]
