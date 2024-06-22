# Write a function called inter_section that takes two lists and finds the intersection (the elements that are present in both lists). 
# The function should return a tuple of intersections. Use list comprehension in your solution. 
# Use the lists below. Your function should return (30, 65, 80).
# list1 = [20, 30, 60, 65, 75, 80, 85] list2 = [42, 30, 80, 65, 68, 88, 95]

def inter_section(list_1, list_2):
    common_numbers = tuple([num for num in list_1 if num in list_2])
    return common_numbers

print(inter_section([20, 30, 60, 65, 75, 80, 85], [42, 30, 80, 65, 68, 88, 95]))
