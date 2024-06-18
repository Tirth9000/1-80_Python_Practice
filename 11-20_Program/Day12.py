# Write a function called zeroed code that takes a list of numbers as an argument. 
# The code should zero (0) the first and the last number in the list. 
# For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0].

def zeroed_code(number_list):
    number_list[0] = 0
    number_list[len(number_list) - 1] = 0

    return number_list

number_list = [2, 5, 7, 8, 9]
print(zeroed_code(number_list))