
# Write a function called sum_list with one parameter that takes a nested list of integers as an argument 
# and returns the sum of the integers. 
# For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33.

def sum_list(nest_list):
    list_total = 0
    for list in nest_list:
        list_total += sum(list)
    
    return print(list_total)

sum_list([[2, 4, 5, 6], [2, 3, 5, 6]])
        
