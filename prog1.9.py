def print_number_pattern(rows):
    for i in range(1, rows + 1):
        # Use nested loop to print repeated numbers
        for j in range(i):
            print(i, end=" ")
        print()  # Move to the next line after printing each row

# Get user input for the number of rows
num_rows = int(input("Enter the number of rows for the pattern: "))

# Print the number pattern
print_number_pattern(num_rows)

