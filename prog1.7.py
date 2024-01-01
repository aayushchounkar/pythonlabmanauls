def calculate_factorial(n):
    factorial = 1

    # Check if the input is negative
    if n < 0:
        return "Factorial is not defined for negative numbers."

    # Calculate factorial using a for loop
    for i in range(1, n + 1):
        factorial *= i

    return factorial

# Get user input for the number
number = int(input("Enter a number: "))

# Calculate and print the factorial
result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")

