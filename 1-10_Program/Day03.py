# Write a function called convert_add that takes a list of strings as an argument and 
# converts it to integers and sums the list. 
# For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

def convert_add(list_string):
    sum = 0
    for string in list_string:
        sum += int(string)
    
    return sum

print(convert_add(['1', '3', '5']))