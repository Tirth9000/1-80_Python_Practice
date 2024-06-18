# Create a simple calculator. 
# The calculator should be able to perform basic math operations, add, subtract, divide and multiply. 
# The calculator should take input from users. 
# The calculator should be able to handle ZeroDivisionError, NameError, and ValueError.

def simple_calculator():
    try: 
        try:
            value1 = int(input("Enter the first value : "))
            value2 = int(input("Enter the second value : "))
        except ValueError as e:
            return print(e)

        operator = input("Enter the operator : ")

        if operator == '+':
            print(f"Addition of {value1} + {value2} = {value1+value2}")
        elif operator == '-':
            print(f"Addition of {value1} - {value2} = {value1-value2}")
        elif operator == '*':
            print(f"Addition of {value1} * {value2} = {value1*value2}")
        elif operator == '/':
            try:
                divide = value1/value2
                print(f"Divide of {value1}/{value2} = {value1/value2}")
            except ZeroDivisionError:
                return print("Division by zero is not supported!")
        else:
            print("Invalid Operator")
    
    except NameError as e:
        return print(e)

simple_calculator()