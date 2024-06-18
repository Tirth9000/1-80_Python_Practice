# Write a function called longest_value that takes a dictionary as an argument 
# and returns the first longest value of the dictionary. 
# For example, the following dictionary should return – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(dic):
    dic_values = list(dic.values())

    max_length = max(len(str(value)) for value in dic_values)

    for value in dic_values:
        if len(str(value)) == max_length:
            return value
 
    
dic = { 
       'a' : 'apple',
       'b' : 'orange',
       'c' : 'red',
       'd' : 'banana'
       }

print(longest_value(dic))
