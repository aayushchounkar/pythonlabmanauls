# Arithmetic operators
def arithmetic_operations(a, b):
    print("Arithmetic Operations:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} ** {b} = {a ** b}")

# Relational operators
def relational_operations(a, b):
    print("\nRelational Operations:")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} >= {b}: {a >= b}")

# Input values
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform arithmetic operations
arithmetic_operations(num1, num2)

# Perform relational operations
relational_operations(num1, num2)
