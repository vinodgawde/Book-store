from Admin import *

def login():
    print(("=")*30);
    print("Welcome to Book Store!")
    print(("=")*30);
    main = input("Enter your Choice to Login.\n1.ADMIN\n2.USER\n")
    if main == "1":
        admin()
            
    if main == "2":
        user()


def admin():
    welcome = input("Do you have an Admin account? (YES/NO) : \n")
    if welcome == "NO":
        while True:
            print("Register as Admin")
            username  = input("Enter admin username:")
            password  = input("Enter admin password:")
            password1 = input("Confirm admin password:")
            if password == password1:
                file = open(username+".txt", "w")
                file.write(username+":"+password)
                file.close()
                print(("=")*35);
                print("Welcome to Book Store! Login Now..")
                print(("=")*35);
                welcome = "YES"
                break
            print("Passwords do not match! Try Again")
    

    if welcome == "YES":
        while True:
            login1 = input("Admin Username:")
            login2 = input("Admin Password:")
            file = open(login1+".txt", "r")
            data = file.readline()
            file.close()
            if data == login1+":"+login2:
                print("Welcome")
                ad_menu()
                break
            print("Incorrect Admin username or password.")


def user():
    welcome = input("Do you have an user account? (YES/NO) : \n")
    if welcome == "NO":
        while True:
            username  = input("Enter your username:")
            password  = input("Enter your password:")
            password1 = input("Confirm your password:")
            if password == password1:
                file = open(username+".txt", "w")
                file.write(username+":"+password)
                file.close()
                print(("=")*35);
                print("Welcome to Book Store! Login Now..")
                print(("=")*35);
                welcome = "YES"
                break
            print("Passwords do not match!")
    

    if welcome == "YES":
        while True:
            login1 = input("Username:")
            login2 = input("Password:")
            file = open(login1+".txt", "r")
            data = file.readline()
            file.close()
            if data == login1+":"+login2:
                print("Welcome")
                u_menu()
                break
            print("Incorrect username or password.")