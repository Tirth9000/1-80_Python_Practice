# Write a function called string_range that takes a single number and returns a string of its range. 
# The string characters should be separated by dots(.) 
# For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

def string_range(num_range):
    num_string = ''
    for number in range(num_range):
        num_string += str(number)
        if number == num_range-1:
            break
        num_string += '.'
    print(num_string)


string_range(6)