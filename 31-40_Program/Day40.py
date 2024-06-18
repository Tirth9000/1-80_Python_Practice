# Write a function called make_tuples that takes two lists, equal lists, and combines them into a list of tuples. 
# For example, if list a is [1,2,3,4] and list b is [5,6,7,8], 
# your function should return [(1,5), (2,6), (3,7), (4,8)].

def make_tuples(list_a, list_b):
    if len(list_a) != len(list_b):
        return print("Invalid length of the list.")

    tuple_list = []
    for n in range(len(list_a)):
        tuple_list.append((list_a[n], list_b[n]))

    return tuple_list

print(make_tuples([1,2,3,4], [5,6,7,8]))