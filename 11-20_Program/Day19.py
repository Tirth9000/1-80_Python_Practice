# Write a function called hide_password that takes no parameters. 
# The function takes an input (a password) from a user and returns a hidden password. 

# For example, if the user enters 'hello' as a password the function should return '****' as a password 
# and tell the user that the password is 4 characters long.

def hide_password():
    password = input("Enter the Password: ")
    word_dic = {}
    hidden_pass = ''
    for i in password:
        if i not in word_dic.keys():
            word_dic[i] = 1
        else:
            word_dic[i] += 1
    
    pass_count = len(word_dic.keys())  

    for i in range(pass_count):
        hidden_pass += '*'

    print(f'Password: {hidden_pass}')
    print(f'Password is of {pass_count} characters long.')
        
hide_password()
