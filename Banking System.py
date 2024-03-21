class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)


def display_info(self):
    print("#######################")
    print("First Name: ", self.first_name)
    print("Last Name: ", self.last_name)
    print("Gender: ", self.gender)
    print("Street Address: ", self.street_address)
    print("City: ", self.city)
    print("Email: ", self.email)
    print("Credit Card Number: ", self.cc_number)
    print("Credit Card Type: ", self.cc_type)
    print("Balance: ", self.balance)
    print("Account Number: ", self.account_no)
    print("#######################")


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser():
    # COMPLETED
    user_to_find = input("Enter the name of the user you want to find: ").title()
    for user in userList:
        full_name = f"{user.first_name} {user.last_name}"
        if full_name == user_to_find:
            display_info(user)
            return
    print("Sorry, no user was found for that name")
    return None
# True


def overdrafts():
    # COMPLETED
    for user in userList:
        if user.balance < 0:
            print("#######################")
            print(f"{user.first_name} {user.last_name} has an overdraft of {user.balance}")
    if len(overdrafts) == 0:
        print("No overdrafts found")
        return
#True


def missingEmails():
    # TO COMPLETE
    for user in userList:
        if user.email == "":
            print("#######################")
            print(f"{user.first_name} {user.last_name} is missing an email")

#True


def bankDetails():
    # TO COMPLETE
    total_users = len(userList)
    print(f"Total number of users: {total_users}")
    total_worth = (sum([]))

    # True
    
def transfer():
    # TO COMPLETE

    True

userList = []          
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()
    
    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()      
    print()
