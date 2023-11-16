# Project_4: password generator

import string
import random

characters = list(
    string.ascii_letters + string.digits + "!@#$%^&*")  # combining a list of alphabet letters, digital signs and other signs into a list

def generate_password():
    while True:
        try:
            password_length = int(input("Enter the length for the password: "))
            break
        except ValueError:
            print(f"It is not a number. Try again!")

    random.shuffle(characters)  # random shuffling of characters in the list

    password = []

    for c in range(password_length):
        password.append(random.choice(characters))

    print("Your password: " + "".join(password))

def user_option():
    option = input("Do you want generate password? (yes/no): ")  # option for user
    edit_option = option.strip()
    if edit_option.lower() == "yes":
        generate_password()
    elif edit_option.lower() == "no":
        print("Program ended.")
        quit()
    else:
        print("Invalid input, please input Yes or No!")
        user_option()


user_option()