#Define a function named perform_operation.

def perform_operation(num1, num2, operation):
    # Convert the operation to lowercase to handle case insensitivity
    operation = operation.lower()
    
    # Check the operation and perform the corresponding arithmetic operation
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
