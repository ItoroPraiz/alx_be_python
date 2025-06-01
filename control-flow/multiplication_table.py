number = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication table for {number}:")  
for X in range(1, 11):
    Z = number * X
    print(f"{number} * {X} = {Z}")  # Display the multiplication result
