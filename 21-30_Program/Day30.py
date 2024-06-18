# Write a function called your_age. 
# This function asks a student to enter their name and then it returns their age. 

# For example, if a user enters Peter as their name, your function should return, 
# ‘Hi, Peter, you are 27 years old.' 

# This function reads data from the database (dictionary below). 
# If the name is not in the dictionary, your code should tell the user that their name is not in the dictionary, 
# and ask them for their age. Your code should then add the name and age to the dictionary of names_age below. 
# Once added your code should return to the user ‘Hi, (added name), you are (added age) years old’. 
# Remember to convert the input from user to lowercase letters

# names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}

names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

def your_age():

    student_name = (input("Enter student name: ")).lower()

    if student_name in names_age: 
        student_age = names_age[student_name]
    else:
        print("Your not in the dictionary, please enter, ")
        new_student = (input("Enter new student name: ")).lower()
        student_age = int(input("Enter student age: "))
        names_age[new_student] = student_age

    print(f'Hi, {student_name.capitalize()}, you are {names_age[student_name]} years old.')
    print(names_age)


your_age()
