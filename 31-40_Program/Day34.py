# names = [ "Peter", "Jon", "Andrew"]

# Write a function called sort_length that takes a list of strings as an argument, 
# and sorts the strings in ascending order according to their length. For example, 
# the list above should return:

# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions


def sort_length(string_list):
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) > len(string_list[j]):
                string_list[i], string_list[j] = string_list[j], string_list[i]

    return string_list

names = ["Peter", "Jon", "Andrew"]
print(sort_length(names))

