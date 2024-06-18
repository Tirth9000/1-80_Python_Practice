# Write a function called user_name, that creates a username for the user. 
# The function should ask a user to input their name. 
# The function should then reverse the name and attach a randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.

import random

def user_name():
    input_name = input("Enter your name: ")

    user_name = input_name + str(random.randint(1000, 9999))

    return user_name

print(user_name())
