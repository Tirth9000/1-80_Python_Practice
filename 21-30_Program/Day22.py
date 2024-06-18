# Write a function called swap_values. 
# This function takes a list of numbers and swaps the first element with the last element. 

# For example, if you pass [2, 4,67, 7] as a parameter, your function should return
# [7, 4, 67, 2].

def swap_values(number_list):
    temp = number_list[0] 
    number_list[0] = number_list[len(number_list)-1] 
    number_list[len(number_list)-1] = temp
    
    return number_list

number = [3, 2, 4, 67, 7, 9, 0]
print(swap_values(number))