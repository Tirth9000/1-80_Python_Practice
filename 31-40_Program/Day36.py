# Write a function called add_reverse. 
# This function takes two lists as argument and adds each corresponding number, and reverses the outcome. 
# For example, if you pass [10, 12, 34] and [12, 56, 78]. Your code should return [112, 22, 68]. 
# If the two lists are not of equal lengths, the code should return a message that "the lists are not of equal lengths".

import numpy as np

def add_reverse(list1, list2):
    add_list = np.array(list1) + np.array(list2)

    return add_list[::-1]

print(add_reverse([10, 12, 34], [12, 56, 78]))

    