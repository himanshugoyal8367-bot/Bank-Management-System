import utils

def statement():
    name = input("Enter name of user: ")
    if name in utils.users:
        if name in utils.history:
            for record in utils.history[name]:
                print(record)
        else:
            print("No transaction history")
    else:
        print("User not found")