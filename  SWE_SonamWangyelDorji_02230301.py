#Reference link : https://www.youtube.com/watch?v=AVOx7lvqhY4
#https://www.youtube.com/watch?v=jABj-SEhtBc
import json
import getpass


passwords = {}

def s_password():
    account = input("Enter the account name: ")
    password = getpass.getpass("Enter the password: ")
    passwords[account] = password
    save_data()

def r_password():
    account = input("Enter the account name: ")
    if account in passwords:
        print("Password:", passwords[account])
    else:
        print("Account not found.")

def save_data():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)
    print("Passwords saved successfully.")

def load_data():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}

def main():
    global passwords
    passwords = load_data()

    while True:
        print("\nOptions:")
        print("1. Save a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            s_password()
        elif choice == "2":
            r_password()
        elif choice == "3":
            save_data()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()