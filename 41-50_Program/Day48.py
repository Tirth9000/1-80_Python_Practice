# str1 = "the love is real"
# Write a function called read_backwards that takes a string as an argument and reverses it. 
# For example, the string above should return: "real is love the"


def read_backwards(string):
    string_list = string.split(' ')
    reversed_string = ''
    
    reversed_string = " ".join(string_list[::-1])
        
    return reversed_string

print(read_backwards("the love is real"))
