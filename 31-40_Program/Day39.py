# str1 = 'leArning is hard, bUt if You appLy youRself ' \
# 'you can achieVe success'

# You are given a string of words. Some of the words in the string contain uppercase letters. 
# Write a code that will return all the words that have an uppercase letter. 
# Your code should return a list of the words. Each word in the list should be reversed. 
# Here is how your output should look:

# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']


def reversed_list(string):
    rev_list = []
    string_list = string.split(' ')
    for words in string_list:
        flag = 0
        for word in words:
            if word.isupper():
                flag = 1
            
        if flag == 1:
            rev_list.append(words[::-1])
            

    return rev_list 

string = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'
print(reversed_list(string))
            