
# Write a function called password_validator. The function asks the user to enter a password. 
# A valid password should have at least one upper letter, one lower letter, and one number. 
# It should not be less than 8 characters long. When the user enters a password, the function should check if the password is valid. 
# If the password is valid, the function should return the valid password. 
# If the password is not valid, the function should tell the users the errors in the password and prompt the user to enter another password.
# The code should only stop once the user enters a valid password. (use while loop).

def password_validator():
    while(True):
        user_password = input("Enter your password : ")
        upper_flag = 0
        lower_flag = 0
        digit_flag = 0
        for letter in user_password:
            if letter.isupper():
                upper_flag = 1
            elif letter.islower():
                lower_flag = 1
            elif letter.isdigit():
                digit_flag = 1
            
        if upper_flag != 1:
            print("Password should contain at least one upper letter.")
            print("Re-enter the password.")
        elif lower_flag != 1:
            print("Password shoult contain at least one lower letter.")
            print('Re-enter the password.')
        elif digit_flag != 1:
            print('Password should contain at least one number.')
            print('Re-enter the password.')
        else:
            return print('Valid Password.')

password_validator()
