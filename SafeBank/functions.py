def read_info():
    """ Reads user's info from txt """

    file = open("c:\\Users\\92per\\coding\\tasks\\SafeBank\\accounts.txt",'r')
    clients_info = []

    for line in file:

        data = line.strip().split(' ')
        name = data[0]
        surname = data[1]
        year_of_birth = int(data[2])
        balance = int(data[3])

        person_info = {"Name": name,
                       "Surname": surname, 
                       "Year of Birth": year_of_birth, 
                       "Balance": balance}

        clients_info.append(person_info)

    return clients_info


def get_user():
    """ Get user input """

    name =input("First Name: ")
    surname = input("Surname: ")

    while True:

        try:
            year_of_birth = int(input("Year of birth: "))
            break

        except ValueError:
            print("Your age must be a number.")

    user = {"Name" : name, "Surname" : surname, "Year of Birth" : year_of_birth}
    return user


def login():
    """ Checks if user in DB """
    people_info = read_info()
    user_recognition = False

    while user_recognition is False:
        user = get_user()

        for person in people_info:

            if all(user[key] == person[key] for key in ["Name", "Surname", "Year of Birth"]):
                print(f"User recognized. Welcome {user['Name']}")
                user_recognition = True
                return person

        if not user_recognition:
            print("We don't have your name in our database.")


def create_account():
    """Creates an account"""

    print("Give us your details and ammount to deposit to open an account.")
    user = get_user()

    try:
        balance = int(input("Please tell us the ammount desired to deposit:"))
    except ValueError:
        print("Please introduce a number.")

    info = {"Balance": balance}
    user.update(info)
    return user


def update_file(people_list):
    """ Adds user to file accounts.txt """

    file = open("c:\\Users\\92per\\coding\\tasks\\SafeBank\\accounts.txt", "w")

    for person in people_list:
        info = f"{person['Name']} {person['Surname']} {person['Year of Birth']} {person['Balance']}\n"
        file.write(info)

    return people_list



def deposit_money(user , people_info):
    """ Deposits money into account """
    try:
        deposit = int(input("Enter the value to deposit: "))

    except ValueError:
        print("Please enter a number.")

    for person in people_info:

        if all(user[key] == person[key] for key in ["Name", "Surname", "Year of Birth"]):
            user["Balance"] += deposit
            person["Balance"] = user["Balance"]

    return user, people_info

def withdraw_money(user, people_info):
    """Withdraws money from account"""
    withdraw = float('inf')

    while True:

        try:
            withdraw = int(input("Enter the value to withdraw: "))

        except ValueError:
            print("Please enter a number.")

        if withdraw > user['Balance']:
            print("You don't have that ammount.")

        else:
            break

    for person in people_info:

        if all(user[key] == person[key] for key in ["Name", "Surname", "Year of Birth"]):
            user["Balance"] -= withdraw
            person['Balance'] = user['Balance']

    return user, people_info
