# Write a function called sort_words that takes a string of words as an argument, removes the whitespaces, and
# returns a list of letters sorted in alphabetical order. Letters will be separated by commas. 
# All letters should appear once in the list. This means that you sort and remove duplicates. 
# For example ‘love life’ should return as ['e,f,i,l,o,v'].

def sort_word(string):
    seperated_string = string.split()
    single_string = ''
    non_repeat = []

    for words in seperated_string:
        for letter in words:
            if letter in non_repeat:
                continue
            else:
                non_repeat.append(letter)

    non_repeat.sort()

    for letter in non_repeat:
        single_string += letter
    
    comma_string = ','.join(letter for letter in single_string)

    return [comma_string]
        
        

print(sort_word('love life'))