# Write a function called index_position. This function takes a string as a parameter and 
# returns the positions or indexes of all lower letters in the string. 

# For example, ‘LovE’ should return [1,2].

def index_position(string):
    lower_index = []
    
    for letter in string:
        if letter.islower():
            lower_index.append(string.index(letter))
            
    return lower_index

print(index_position('LovE You'))

