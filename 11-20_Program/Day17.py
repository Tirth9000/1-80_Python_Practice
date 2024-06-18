# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. 
# For example, if you pass ‘23569’ as an argument, your function should return 9. Use list comprehension.

def biggest_odd(number_string):
    list_odd = []
    for number in number_string:
        if int(number)%2 != 0:
            list_odd.append(int(number))
    
    return max(list_odd)

print(biggest_odd('23569'))
