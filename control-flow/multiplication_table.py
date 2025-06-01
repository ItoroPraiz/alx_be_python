number = int(input("Enter a number to see its multiplication table: "))
'''Use a for loop to iterate from 1 to 10 (inclusive) and print 
the multiplication table for the given number.'''
print(f"Multiplication table for {number}:")  
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")