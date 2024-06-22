# Write a function called find_index that takes two arguments; a list of integers, and an integer. 
# The function should return the indexes of the integer in the list. 
# If the integer is not in the list, the function should convert all the numbers in the list into the given integer.

# For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7, your code should return [4, 5] as the indexes of 7 in the list. 
# If the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should return [8, 8, 8, 8, 8, 8] because 8 is not in the list.

def find_index(list_int, integer):
    int_index = []
    index_flag = 0
    for num in range(len(list_int)):
        if list_int[num] == integer:
            index_flag = 1
            int_index.append(num)
        else:
            list_int[num] = integer

    if index_flag:
        return int_index
    else:
        return list_int


print(find_index([1, 2, 4, 6, 7, 7], 7))