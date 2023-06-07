#Password generator

import random
import string

symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '_']

print("\nWelcome to the password generator.\n")

# Prompt the user for the desired number of each character type
while True:
    capital_letters_number = int(input("How many capital letters do you want in your password? "))
    lowercase_letters_number = int(input("How many lowercase letters do you want in your password? "))
    numbers_number = int(input("How many numbers do you want in your password? "))
    symbols_number = int(input("How many symbols do you want in your password? "))
    
    # Check if all the entered numbers are positive integers
    if all(num > 0 for num in [capital_letters_number, lowercase_letters_number, numbers_number, symbols_number]):
        break
    else:
        print("Invalid input. The numbers should be positive integers.")

# Create a list with the desired characters for the password
password_list = random.sample(string.ascii_uppercase, capital_letters_number) + \
               random.sample(string.ascii_lowercase, lowercase_letters_number) + \
               random.sample(string.digits, numbers_number) + \
               random.sample(symbols, symbols_number)

# Randomly shuffle the characters in the password list
random.shuffle(password_list)

# Concatenate the shuffled characters to form the password
password = ''.join(password_list)

# Print the generated password
print(f"\nYour password is:\n\n{password}\n")
