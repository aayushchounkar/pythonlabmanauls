def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    return sum_of_digits == number

# Input a number
num = int(input("Enter a number: "))

# Check if the entered number is an Armstrong number
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
