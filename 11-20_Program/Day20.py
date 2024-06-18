# Your new company has a list of figures saved in a list. The issue is that these numbers have no separator.
 
# The numbers are saved in the following format:
# [1000000, 2356989, 2354672, 9878098].

# You have been asked to write a code that will convert each of the numbers in the list into a string. 
# Your code should then add a comma on each number as a thousand separator for readability. 

# When you run your code on the above list, your output should be:
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098']

# Write a function called convert_numbers that will take one argument, a list of numbers above.


def convert_numbers(number_list):
    count = 0
    new_num = ''
    new_num_list = []
    for number in number_list:
        count = 0
        for i in range(len(str(number))-1, -1, -1): 
            if count == 2:
                new_num += (str(number)[i]+',')
                count = 0
            else:
                new_num += (str(number)[i])
                count += 1

        new_num_list.append(new_num[::-1])
        new_num = ''
    
    return new_num_list
    
if __name__ == '__main__':
    print(convert_numbers([1000000, 2356989, 2354672, 9878098]))
