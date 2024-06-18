# Write a function called check_duplicates that takes a list of strings as an argument. 
# The function should check if the list has any duplicates. 
# If there are duplicates, the function should return the duplicates. 
# If there are no duplicates, the function should return "No duplicates". 
# For example, the list of fruits below should return apple as a duplicate and 
# list of names should return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple'] names = ['Yoda', 'Moses', 'Joshua', 'Mark']


def check_duplicates(list_string):

    for i in range(len(list_string)):
        for j in range(i+1, len(list_string)):
            if list_string[i] == list_string[j]:
                return list_string[i]
        
    return "no duplicates"


print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
print(check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']))

            