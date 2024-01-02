def main_menu():
    """ Main menu """

    print("1. Login existing account.")
    print("2. Create new account.")
    print("3. Check Balance.")
    print("4. Deposit money.")
    print("5. Withdraw money.")
    print("6. Checking account Limit.")
    print("7. Exit.")

    try:
        option = int(input("Choose an option: "))

    except ValueError:

        print("Please enter a valid option.")

    return option

