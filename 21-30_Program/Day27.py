# Write a function called flat_list that takes one argument, a nested list. 
# The function converts the nested list into a one- dimension list. 
# For example [[2,4,5,6]] should return [2,4,5,6].

def flat_list(nested_list):
    one_dlist = []
    for list in nested_list:
        one_dlist += list
    
    return one_dlist

nest_list = [[1,2,3,4], [2,4,5,6]]

print(flat_list(nest_list))