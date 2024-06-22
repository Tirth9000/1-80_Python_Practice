# Write a function called count that takes one argument a string, and 
# returns a dictionary of how many times each element appears in the string. 
# For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(string):
    count_dic = {}
    for word in string:
        if word not in count_dic:
            count_dic[word] = 1
        else:
            count_dic[word] += 1
    return count_dic
            
print(count('hello'))