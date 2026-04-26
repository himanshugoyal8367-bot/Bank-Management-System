import utils

def deposit_money():
    name = input("Enter name of the user: ")
    if name in utils.users:
        amount = float(input("Enter the amount you want to deposit: "))
        utils.users[name] += amount
        print("Amount deposited successfully!")
        utils.history[name].append(f"{name} Deposited ₹ {amount}")
    else:
        print("User not found")