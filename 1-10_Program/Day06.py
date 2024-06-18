# You are given a list of names above. This list is made up of names of lowercase and uppercase letters. 
# Your task is to write a code that will return a tuple of all the names in the list 
# that have only lowercase letters. Your tuple should have names sorted alphabetically in descending order. 

# names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

# Using the list above, your code should return:
# ('kerry', 'dickson', 'carol', 'adam')

def list_lowercase(names):
    lowercase_names = []
    for name in names:
        if name.islower():
            lowercase_names.append(name)
        
    lowercase_names.sort(reverse=True)
    lowercase_names = tuple(lowercase_names)

    print(lowercase_names)

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
list_lowercase(names)