import random
import string

MIN_LENGTH = 1
SYMBOLS = "!@#$%&*"
letters = string.ascii_letters + string.digits + SYMBOLS

password_history = []

def make_password(length):
    password = ""

    for i in range(length):
        password = password + random.choice(letters)

    return password


print("Welcome! This program makes a random password.")

again = "yes"

while again == "yes":

    try:
        length = int(input("How many characters do you want? "))

        if length >= MIN_LENGTH:
            password = make_password(length)

            print("Your random password is:", password)

            password_history.append(password)

            try:
                file = open("password_history.txt", "a")
                file.write(password + "\n")
                file.close()

            except OSError:
                print("Could not save the password.")

            else:
                print("Password saved!")

            finally:
                print("Done saving.")

        else:
            print("That is not a valid number. Try again.")

    except ValueError:
        print("Please enter a number.")

    else:
        print("Finished checking.")

    finally:
        print("Thank you for using the program.")

    again = input("Do you want another password? Type yes or no: ")
    again = again.lower()

print("Your password history:")

for password in password_history:
    print(password)

print("bye bye")