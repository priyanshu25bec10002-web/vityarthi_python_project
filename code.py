import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    
    symbols = "@#!$%^&*"

    
    characters = letters
    password = []

    
    if use_digits:
        password.append(random.choice(digits))
        characters += digits
    if use_symbols:
        password.append(random.choice(symbols))
        characters += symbols

    
    remaining_length = length - len(password)
    password += random.choices(characters, k=remaining_length)

    
    random.shuffle(password)
    return "".join(password)



try:
    length = int(input("Enter password length: "))
    digits_choice = input("Include digits? (y/n): ").lower() == 'y'
    symbols_choice = input("Include symbols? (y/n): ").lower() == 'y'

    if length < 1:
        print("Password length must be at least 1")
    else:
        password = generate_password(length, digits_choice, symbols_choice)
        print("\n🔐 Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
