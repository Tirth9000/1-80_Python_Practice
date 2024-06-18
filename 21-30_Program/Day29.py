# Write a function called same_in_reverse that takes a string and checks if the string reads the same in reverse. 
# If it is the same, the code should return True if not, it should return False. 
# For example, ‘dad’ should return True, because it reads the same in reverse.

def same_in_reverse(word_string):
    if word_string == word_string[::-1]:
        return True
    else:
        return False


print(same_in_reverse('dad'))
print(same_in_reverse('dada'))
