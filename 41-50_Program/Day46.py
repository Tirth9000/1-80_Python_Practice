# Write a function called nested_lists that takes any number of lists and creates a 2-dimensional nested list of lists. 

# For example, if you pass the following lists as arguments: [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5].
# Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]

def nested_lists(*args):
    nested_list = list(args)
    return nested_list

print(nested_lists( [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))