
import random
import string

print("Welcome! This program makes a random password.")

again = "yes"

while again == "yes":

    length = input("How many characters do you want in your password? ")

    if length.isdigit() and int(length) > 0:
        length = int(length)

        letters = string.ascii_letters + string.digits + "!@#$%&*"
        password = ""

        for i in range(length):
            character = random.choice(letters)
            password = password + character

        print("Your random password is:", password)

    else:
        print("That is not a valid number. Try again.")
        continue

    again = input("Do you want another password? Type yes or no: ")
    again = again.lower()

print("Goodbye!")
