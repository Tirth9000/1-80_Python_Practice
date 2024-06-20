# Write a function called largest_number that takes a list of integers and 
# re-arrange the individual digits to create the largest number possible. 

# For example, if you pass the following as an argument: list1 = [3, 67, 87, 9, 2]. 
# Your code should return the number in this exact format: 9,877,632 as the largest number.


def largest_number(int_list):
    int_string = ''.join([str(number) for number in int_list])
    seperate_int = [int(number) for number in int_string]
    seperate_int.sort(reverse = True)

    seperate = "".join(str(number) for number in seperate_int)
    largest_num = f"{int(seperate):,}"

    return largest_num

print(largest_number([3, 67, 87, 9, 2]))

