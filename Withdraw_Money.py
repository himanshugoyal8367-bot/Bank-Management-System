import utils

def withdraw_money():
    name = input("Enter name of user: ")
    if name in utils.users:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount <= utils.users[name]:
            utils.users[name] -= amount
            print("Amount withdrawn successfully!")
            utils.history[name].append(f"{name} Withdrawn ₹ {amount}")
        else:
            print("Insufficient Balance")
    else:
        print("User not found")