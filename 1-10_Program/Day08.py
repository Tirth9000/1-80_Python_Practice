# Write a function called word_index that takes one argument, 
# a list of strings and returns the index of the longest word in the list. 
# If there is no longest word (if all the strings are of the same length), the function should return zero (0). 
# For example, the list below should return 2.

# words1 = ["Hate", "remorse", "vengeance"] And this list below, shoul return zero (0)
# words2 = ["Love", "Hate"]


def word_index(words):
    
    length_word = []
    for word in words:
        length_word.append(len(word))
    max_length = max(length_word)
    
    if length_word.count(max_length) > 1:
        return 0 
    else:
        return length_word.index(max_length)



words1 = ["Hate", "remorse", "vengeance"]
print(word_index(words1))

words2 = ["Love", "Hate"]
print(word_index(words2))
