# Write a function called middle_figure that takes two parameters a, and b. 
# The two parameters are strings. The function joins the two strings and finds the middle element. 
# If the combined string has a middle element, the function should return the element, otherwise, return ‘no middle figure’. 

# Use ‘make love’ as an argument for a and ‘not wars’ as an argument for b. 
# Your function should return ‘e’ as the middle element. Whitespaces should be removed.

def middle_figure(a: str, b: str) -> str:
    merge_string = (a + b).replace(" ","")

    if len(merge_string)%2 == 1:
        middle_element = merge_string[len(merge_string)//2]
        return f"Middle element is : {middle_element}"
    else:
        return "No middle figure"
    
print(middle_figure('make love', 'not wars'))


        