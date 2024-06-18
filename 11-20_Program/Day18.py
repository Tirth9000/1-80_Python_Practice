# Write a function called zeros_last. This function takes a list as argument. 
# If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list. 
# If there are no Zeros in the list, the function should return the original list sorted in ascending order. 

# For example, if you pass [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1, 4, 6, 7, 9, 0, 0]. 
# If you pass [2, 1, 4, 7, 6] as your argument, your code should return [1, 2, 4, 6, 7].

def zeros_last(number_list):
    number_list.sort()
    for number in number_list:
        if number == 0:
            number_list.remove(number)
            number_list.append(number)
    
    return number_list


number_list1 = [1, 4, 6, 0, 7,0,9]
print(zeros_last(number_list1))

number_list2 = [2, 1, 4, 7, 6]
print(zeros_last(number_list2))