'''Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
Make sure you use num1 and num2 for first and second numbers'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
'''Ask the user to input an operator using: Enter an operator (+, -, *, /):'''
operator = input("Choose the operation (+, -, *, /):") 
'''Use a match-case statement to perform the operation based on the operator input.
If the operator is not one of the four, print an error message: "Invalid operator."'''
match operator:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator.")
# The match-case statement is used to handle different operations based on the operator input.