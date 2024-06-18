# Write a function called capitalize. 
# This function takes a string as an argument and capitalizes the first letter of each word. 
# For example, ‘i like learning’ becomes ‘I Like Learning’.

def capitalize(string):
    cap_string = ''
    split_string = string.split(' ')

    for st in split_string:
        cap_string += ' ' + st.capitalize()

    return cap_string

print(capitalize('i like learning'))