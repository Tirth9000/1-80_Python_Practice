# Write a function that has one parameter and takes a list of words as an argument. 
# The function returns the longest word from the list. Name the function longest_word. 
# The function should return the longest word and the number of letters in that word. 

# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your function should return
# [10, JavaScript] as the longest word.

def longest_word(list_words: list):
    max_length = len(list_words[0])
    longest_word = []
    for word in range(1, len(list_words)):
        if len(list_words[word]) == max_length:
            max_length = len(list_words[word])
            longest_word.append(max_length)
            longest_word.append(list_words[word])

        elif len(list_words[word]) > max_length:
            max_length = len(list_words[word])
            longest_word.append(max_length)
            longest_word.append(list_words[word])
        
    return longest_word


print(longest_word(['Java', 'JavaScript', 'Python', 'JavaScript']))
            
