# Write a function called count_dots. 
# This function takes a string separated by dots as a parameter and counts how many dots are in the string. 
# For example, ‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots.

def count_dots(dots_string):
    dot_count = dots_string.count('.')
    return dot_count

print(count_dots('h.e.l.p.'))
print(count_dots('he.lp.'))

    