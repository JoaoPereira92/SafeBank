import functions as fc
import menus as m
people_info = fc.read_info()
OPTION = 0
LOGIN = False
print("Hello, welcome to SafeBank!\n")


while OPTION != 7:
    OPTION = m.main_menu()

    if OPTION == 1:
        user = fc.login()
        LOGIN = True

    elif OPTION == 2:
        if LOGIN is False:
            user = fc.create_account()
            people_info.append(user)
        else:
            print("Already logged in.\n")

    elif OPTION == 3:
        if LOGIN is True:
            print(f"Your current balance is {user['Balance']}.\n")
        else:
            print("Not logged in.\n")

    elif OPTION == 4:

        if LOGIN is True:
            user, people_info = fc.deposit_money(user , people_info)
            print(f"Your current balance is {user['Balance']}.\n")
            fc.update_file(people_info)

        else:
            print("Not logged in.\n")

    elif OPTION == 5:
        if LOGIN is True:
            user , new_people_info = fc.withdraw_money(user, people_info)
            print(f"Your current balance is {user['Balance']}.\n")
            fc.update_file(new_people_info)

    elif OPTION == 6:
        fc.update_file(people_info)
        break

    OPTION = 0
