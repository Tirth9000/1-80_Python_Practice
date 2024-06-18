# Write a function called prime_numbers. 
# This function asks a user to enter a number (integer) as an argument and returns a list of all the prime numbers within its range. 
# For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers(number):
    prime_number = []
    for i in range(2, number):
        flag = 0
        for j in range(2, i):
            if i%j == 0:
                flag = 1

        if flag == 0:
            prime_number.append(i)
    print(prime_number)

prime_numbers(10)
