


# this file contains how to take a input from a user and make lower case


print('')  # just adding new blank line space

take_from_user = input()  # just assign a variable for store the user input
print (take_from_user.lower())  # we print that variable which contain the user input value and add a python build in function .lower() to make every thing in input at lower case and print it to the user display
print ("")
print (' what you see on up is what exercise 4.4 tells me to do just take input from user and print all input as lower case')  # just a normal string print

print ('')

# we can make it more better by giving user ahint what to type

print ("i make it little better")
print ('')

user_see = "Type something in mixed case we will be show everything those in lower case : "  # just a variable with string value in it what the user will see
we_take = input(user_see)  # another variable to store that user input into him also shows the last string value on user screen
print("")
print ('You want to get print in lower case : ' + we_take.lower())  # we just add simple string to be print with user input value also after the variable which contain user input we added a python build in function ( .lower() ) to print everything in lower case


# in case you want to add more functionality in your user input then use the blow code as an example


#print ("")
#pop = "Type to show in user display"
#user_input_function = input(pop)
#another_variable = "'" + user_input_function + "'" # now add your another functionality for example i added ( ' '  ) this will shows the ( '' ) before and after user input value
#print ( "Your thoughts " + another_variable.lower())  # we added a sting to show infront of user input value/what we take and refine and the ( .lower() ) lower function to print everything in lower case
