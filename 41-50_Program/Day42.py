# Create three functions.
# The first called add_hash takes a string and adds a hash # between the words. 
# The second function called add_underscore removes the hash (#) and replaces it with an underscore "_". 
# The third function called remove_underscore, removes the underscore and replaces it with nothing. 

# if you pass ‘Python’ as an argument for the three functions, and you call them at the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

def add_hash(string):
    string_hash = ''
    for word in string:
        string_hash += word + '#'
    return string_hash

def add_underscore(string_hash):
    string_under = string_hash.replace('#', '_')
    return string_under

def remove_underscore(string_under):
    string_remove = string_under.replace('_', '')
    return string_remove


print(remove_underscore(add_underscore(add_hash('Python'))))

