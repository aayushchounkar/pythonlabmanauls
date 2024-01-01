def is_vowel(char):
    vowels = "aeiou AEIOU"

    if char in vowels:
        return True
    else:
        return False

# Input a character
character = input("Enter a character: ")

# Check if the entered character is a vowel
if len(character) == 1 and character.isalpha():
    if is_vowel(character):
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is not a vowel.")
else:
    print("Please enter a valid single character.")
