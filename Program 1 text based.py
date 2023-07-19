# Program 1 text based:

# First, create an empty dictionary to store account usernames and passwords, and a set for the food items
Loginfo = {}
menu = {"Chicken sandwich","chicken sandwich"}

# Function to add username and password to the dictionary
def add_password(username, password):
    Loginfo[username] = password 

# Main program logic
def main():
    while True:
        print("C. Create Login and Password")
        print("L. Login")
        print("E. Exit")

        choice = input("Enter your choice: ")

        if choice == "C":
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(username, password)
            print("Account created successfully!")
            print()
            
        elif choice == "L":
            username = input("Username: ")
            password = input("Password: ")
            for i in Loginfo:
                if i == username:
                    if password == Loginfo[i]:
                        print("Successfully logged in")
                        print()
                        print("Select how many items you want")
                        print()
                        print("Chicken sandwich: $10.50")
                        while True:
                            order = input("Type your order: ")
                            if order in menu:
                                print("")
                                print("Total is $10.50")
                                print("")
                                break
                            else:
                                print("Invalid choice")
                    else:
                        print("Incorrect password")
                        break
                    
                else:
                    print("Incorrect username")
                    break

        elif choice == "E":
            break
        else:
            print("Invalid choice, please try again!!")


if __name__ == "__main__":
    main()
