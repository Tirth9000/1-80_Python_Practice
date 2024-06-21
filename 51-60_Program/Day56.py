# Write a function called repeated_name that finds the most repeated name in the following list.
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]

def repeated_name(string_list):
    most_repeate = {}
    for name in string_list:
        if name not in most_repeate:
            most_repeate[name] = 1
        else:
            most_repeate[name] += 1
        
    return max(most_repeate)

names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(names))