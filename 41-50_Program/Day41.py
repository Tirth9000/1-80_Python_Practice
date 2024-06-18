# Write a function called even_or_average that ask a user to input five numbers. 
# Once the user is done, the code should return the largest even number in the inputted numbers. 
# If there is no even number in the list, the code should return the average of all the five numbers.

def even_or_average():
    num_5 = input("Enter any 5 numbers: ")
    max_even = []
    avg_num = 0
    flag = 0

    for num in num_5:
        avg_num += int(num)
        if int(num)%2 == 0:
            flag = 1
            max_even.append(num)
    
    if flag == 1:
        print(f"Maximum even number is {max(max_even)}")
    else:
        print(f"Average of the five numbers is {avg_num/5}")

even_or_average()
        