# Create a function called all_the_same that takes one argument, a string, a list, or a tuple and checks if all the elements are the same. 
# If the elements are the same, the function should return True. 
# If not, it should return False. For example, [‘Mary’, ‘Mary’, ‘Mary’] should return True.

def all_the_same(str_li_tuple):
    string_list = []
    if type(str_li_tuple) == str:
        string_list = str_li_tuple.split(" ")
    else:
        string_list = list(str_li_tuple)

    if string_list.count(string_list[0]) == len(string_list):
        return True
    else:
        return False

print(all_the_same('tirth tirth tirth'))

print(all_the_same(['Mary', 'Mary', 'Mary']))