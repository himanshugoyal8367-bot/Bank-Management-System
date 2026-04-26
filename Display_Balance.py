import utils

def display_balance():
    name = input("Enter name of user: ")
    if name in utils.users:
        print("\t====Your Bank Balance====")
        print("\t\t", utils.users[name])
    else:
        print("User not found")