# s = 'Hi my name is Richard'
# Write a function called string_length that takes a string of words (words and spaces) as argument. 
# This function should return the length of all the words in the string. 
# Return the results in a form of a dictionary. The string above should return:
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}

def string_length(string):
    string_list = string.split()
    word_count = {}

    for word in string_list:
        if word not in word_count.keys():
            word_count[word] = len(word)
        else:
            word_count[word] += 1
    
    return word_count

print(string_length('Hi my name is Tirth'))