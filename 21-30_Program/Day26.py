# Write a function called Python_snakes that takes a number as an argument and creates the following shape, 
# using the number's range: (hint: Use the loops and emoji library. 
# If you pass 7 as argument, your code should print the following:
#                 *
#               *   *
#             *   *   *
#           *   *   *   *
#         *   *   *   *   *
#       *   *   *   *   *   *


def Python_snake(number):

    for i in range(number):
        for k in range(number-i):
            print(" ", end=' ')
        for j in range(i+i):
            if j%2 == 0:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        
        print('\n')

Python_snake(7)