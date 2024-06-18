# Write a function called age_in_minutes that tells a user how old they are in minutes. 
# Your code should ask the user to enter their year of birth, and 
# it should return their age in minutes (by subtracting their year of birth to the current year). 
# Here are things to look out for:

#     a. The user can only input a 4-digit year of birth. 
#     For example, 1930 is a valid year. However, entering any number longer or less than 4 digits long should render input invalid. 
#     Notify the user to input a four digits number.
    
#     b. If a user enters a year before 1900, your code should tell the user that input is invalid. 
#     If the user enters the year after the current year, the code should tell the user, to input a valid year.

# The code should run until the user inputs a valid year. Your function should return the user's age in minutes. 

# For example, if someone enters 1930, as their year of birth your function should return:
# You are 48,355,200 minutes old.

from datetime import datetime
from Day10_10 import *

def age_in_minutes(year_of_birth):
    if year_of_birth < 1900 or len(str(year_of_birth)) < 4:
        print("Invalid Year of Birth : enter the year in 4 digit and should not be less than 1900.")
    else:
        birth_year = datetime(year_of_birth, 1, 1)
        present_year = datetime((datetime.now()).year, 1, 1)

        total_minute = [int((present_year - birth_year).total_seconds() / 60)]
    
    minutes = convert_numbers(total_minute)

    return print(f'You are {minutes[0]} minutes old.')
    

age_in_minutes(1930)