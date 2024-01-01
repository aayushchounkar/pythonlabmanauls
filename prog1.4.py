def print_natural_numbers_and_sum(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Print the first n natural numbers
    print(f"First {n} natural numbers:")
    for i in range(1, n + 1):
        print(i, end=" ")

    # Calculate the sum of the first n natural numbers
    sum_natural_numbers = n * (n + 1) // 2

    # Print the sum
    print(f"\nSum of the first {n} natural numbers: {sum_natural_numbers}")


# Input value for n
n = int(input("Enter a positive integer (n): "))

# Call the function to print natural numbers and their sum
print_natural_numbers_and_sum(n)
