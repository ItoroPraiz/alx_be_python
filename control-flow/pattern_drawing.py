size = int(input("Enter the size of the pattern: "))
'''Use a while loop to print a square pattern of asterisks (*) with the given size.'''
i = 0
while i < size:
    j = 0
    while j < size:
        print("*", end=" ")
        j += 1
    print()  # Move to the next line after printing one row
    i += 1

 

