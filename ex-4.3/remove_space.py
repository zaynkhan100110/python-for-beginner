


     # this file contain how to remove space from a string value


# assigning strings with values in variables

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

# remove white space from the strings of value
string1.lstrip()  # this will remove white spaces rom left side but to see the result you may need python shell normal terminal unable to show the result
string2.rstrip()  # this will remove white spaces rom right side but to see the result you may need python shell normal terminal unable to show the result
string3.strip()   # this will remove white spaces rom both side but to see the result you may need python shell normal terminal unable to show the result

# assigning strings with values in variables

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "


# replace the previous strings with new strings with white space removed
string1_1 = string1.lstrip()  # this remove white spaces from left side
string2_2 = string2.rstrip()  # this remove white spaces from right side
string3_3 = string3.strip()   # this remove white spaces from both side

# just prints
print (string1_1)
print (string2_2)
print (string3_3)

# to confim that white space removed i can print them with quotes by just type variable

# assigning strings with values in variables also added quotes to print with quotes

string4 = " 'Filet Mignon'"
string5 = "'Brisket' "
string6 = " 'Cheeseburger' "


# replace the previous strings with new strings with white space removed
string4_4 = string4.lstrip()  # this remove white spaces from left side
string5_5 = string5.rstrip()  # this remove white spaces from right side
string6_6 = string6.strip()   # this remove white spaces from both side


print (' ')  # added a new blank line space
# simple print to explain
print ('To confirm that the whitespaces actually remove i added quotes before word starts and just after words ends without give hands on spaces')
print (' ')  # added a new blank line space
# just prints
print (string4_4)
print (string5_5)
print (string6_6)


# this was awesome
