# Write a function called equal_strings. The function takes two strings as arguments and compares them.
# If the strings are equal (if they have the same characters and have equal length), it should return True, 
# if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.

def equal_string(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for ch in str1:
            if ch not in str2 or str1.count(ch) != str2.count(ch):
                print('i')
                return False
            else:
                continue
    
    return True

print(equal_string('love', 'evol'))
