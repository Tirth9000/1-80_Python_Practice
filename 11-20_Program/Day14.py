# You are given a list of names, and you are asked to write a code that returns all the names that start with 'S'. 
# Your code should return a dictionary of all the names that start with S and how many times they appear in the dictionary. 

# Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
# Your code should return: {“Sasha”: 1, “Sera”: 2}


def start_S(name_list):
    name_dic = {}
    for name in name_list:
        if name[0] in ('s', 'S'):
            name_dic[name] = name_list.count(name) 
        
    return name_dic

names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
print(start_S(names))