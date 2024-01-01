def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces before the asterisks
        for j in range(rows - i):
            print(" ", end=" ")
        
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end=" ")

        # Move to the next line after printing each row
        print()

# Get user input for the number of rows
num_rows = int(input("Enter the number of rows for the pyramid: "))

# Print the pyramid pattern
print_pyramid(num_rows)

