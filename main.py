from Deposit_Money import deposit_money
from Withdraw_Money import withdraw_money
from Display_Balance import display_balance
from Statement import statement

while True:
    print("\t\tATM Simulation")
    print("==============================\n1. Deposit Money")
    print("==============================\n2. Withdraw Money")
    print("==============================\n3. Display Balance")
    print("==============================\n4. Statements of transaction")
    print("==============================\n5. Exit")
    print("==============================")
    choice = int(input("Enter your choice number you want to do: "))
    if choice == 1:
        deposit_money()
    elif choice == 2:
        withdraw_money()
    elif choice == 3:
        display_balance()
    elif choice == 4:
        statement()
    elif choice == 5:
        print("\nExiting the program....\n")
        break
    else:
        print("Invalid choice! Try again")