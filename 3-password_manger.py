"""Store and encrypt passwords projects"""
from cryptography.fernet import Fernet

# def write_key():
#     """
#     The function `write_key` generates a key using Fernet and writes it to a file named "key.txt".
#     """
#     key = Fernet.generate_key()
#     with open("key.txt", "wb") as f:
#         f.write(key)

# write_key()


def read_key():
    """
    The function `read_key` reads a key from a file named "key.txt" and returns it.
    """
    with open("key.txt", "rb") as f:
        key = f.read()
    return key

key = read_key()

fer = Fernet(key)



def view():
    """
    This function reads a file containing account names and passwords,
    prompts the user to enter an account name, and then displays the
    corresponding password if the account name is found.
    """
    name = input("Enter the name of the account: ")

    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" | ")
            if user == name:
                print(f"Your password is: {fer.decrypt(pwd.encode()).decode()}")
                break
        else:
            print("Account not found.")


def add():
    """
    The function `add` takes user input for an account name and password, and appends them to a file
    named "passwords.txt" in the format "name | password".
    """
    name = input("Enter the name of the account: ")
    pwd = input("Enter the password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("View your passwords or add a new one (View/Add) - press q to quit: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue
