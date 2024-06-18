# Write a function called odd_even that has one parameter and takes a list of numbers as an argument. 
# The function returns the difference between the largest even number in the list and the smallest odd number in the list.
# For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(number_list):
    
    max_even = 0
    min_odd = 0
    for number in number_list:
        if number%2 != 0:
            min_odd = number
            break

    for number in number_list:
        if number%2 == 0:
            if max_even < number:
                max_even = number 
        else:
            if min_odd >= number:
                min_odd = number

    return print(f'{max_even} - {min_odd} =', max_even-min_odd)

odd_even([5,2,4,6,7,10,11,12,20])