# Create a function called average_calories that calculates the average calories intake of a user. 
# The function should ask the user to input their calories intake for any number of days and 
# once they hit 'done' it should calculate and return the average intake.

def average_calories():
    day = 1
    calorie_count = 0
    print("Enter 'done' to finish the count.")
    while True:
        choice = input(f"Enter Day {day} calorie intake: ")
        if choice == 'done':
            break
        day += 1
        calorie_count += int(choice)

    return print(f"Average calories intake of {day-1} days is {calorie_count//(day-1)}")

average_calories()