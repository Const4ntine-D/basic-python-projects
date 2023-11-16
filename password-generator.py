# Project_4: password generator

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*") # combining a list of alphabet letters, digital signs and other signs into a list


def generate_password():
    password_length = int(input("How long would you like your password to be?"))

    random.shuffle(characters) # random shuffling of characters in the list

    password = []

    for c in range(password_length):
        password.append(random.choice(characters))
    
    print("".join(password))



option = input("Do you want generate password again? (yes/no)") # option for user
if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input Yes or No!")
    quit()

