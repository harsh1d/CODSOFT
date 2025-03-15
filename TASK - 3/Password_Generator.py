"""
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
"""
""" User Input: Prompt the user to specify the desired length of the
 password.
 Generate Password: Use a combination of random characters to
 generate a password of the specified length.
 Display the Password: Print the generated password on the screen.
"""
import string
import random
import datetime
import os
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    start_time = datetime.datetime.now()
    timestamp = start_time.strftime("%d-%m-%Y_Time = %H%M-%S")
    folder_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder_path, f"Passwords_{timestamp}.txt")
    with open(filename, 'w') as file:
        password_count = 1
        while True:
            try:
                length = int(input("Enter the desired length for the password: "))
                if length <= 0:
                    print("Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}")
            file.write(f"password {password_count} = {password}\n")
            password_count += 1

            repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if repeat != 'yes':
                break
        file.write(f"\nGenerated on: {timestamp}\n")

if __name__ == "__main__":
    main()
