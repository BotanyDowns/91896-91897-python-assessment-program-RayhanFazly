#Programe 2 final text based
print("")
print("|=======================================================|")
print("Hello welcome to coffee cafe please choose the following")#title of the text based program
print("|=======================================================|")
print("")

#create a empity dictionary to store user and pass and 2 dictionary list which are food and drink items with prices
Loginfo = {}
menuF = {"Breakfast Sandwich": 10.50, "breakfast sandwich": 10.50, "Steak And Cheese Pie": 5.00,
         "steak and cheese pie": 5.00, "Croissant":3.50, "croissant":3.50, "Cupcake":6.00, "cupcake": 6.00}

menuD = {"Espresso": 8.00, "espresso":8.00, "Latte":3.00 ,"latte": 3.00, "Ice Coffee":5.00 ,"ice coffee": 5.00,
         "Water": 0.50, "water": 0.50}


#adding 2 functions
def add_password(username, password):
    Loginfo[username] = password

def main():
    while True:
#making three options for the user 
        print("C. Create Login")
        print("L. Login")
        print("E. Exit")

        print("")
        choice = input("Enter your choice: ")
        print("")
        if choice == "C":
            username = input("Create username: ")
            password = input("Create password: ")
            add_password(username, password)
            print("")
            print("|------------------------------|")
            print("Account created successfully!")
            print("|------------------------------|")
            print("")
            
        elif choice == "L": #elif statement is where user can have another choice 
            username = input("Enter username: ")
            password = input("Enter password: ")
            for i in Loginfo:
                if i == username:
                    if password == Loginfo[i]:
                        #below here is where alot of print() is used and its helps to customise how ur gonna text based lay out is gonna go
                        print("")
                        print("|----------------------|")
                        print("Sucessfully logged in")
                        print("|----------------------|")
                        print("")
                        print("")
                        print("Hello welcome to coffee call cafe")
                        print("Heres our MENU")
                        print("")
                        print("|--------------------------------------Breakfast--------------------------------------|")#menuF - menu foods
                        print("Breakfast Sandwich: $10.50", 
                              "Steak And Cheese Pie: $5.00",
                              "Croissant: $3.50",
                              "Cupcake: $6.00")
                        print("|-------------------------------------------------------------------------------------|")
                        print("")
                        print("|---------------------------Drinks--------------------------|")#menuD - menu drinks
                        print("Espresso: $8.00",
                              "Latte: $3.00",
                              "Ice Coffee: $5.00",
                              "Water: 0.50c")
                        print("|-----------------------------------------------------------|")
                        print("")
                
                        decisionF = ""
                        countF = 0 #coutning the quantity of each item when user inputs 
                        totalF = 0 #the total amount of when user inputs many items or 1 
                        while True:
                            itemF = input("Please type in your selction of choice of breakfast: ")
                            if itemF in menuF:
                                totalF += menuF[itemF]
                                countF += 1
                            else:
                                print("Incorrect spelling, try select again 'optional'")
 #here im using decision statement where the program will ask user to make a decision on if they want more or no 
                            decisionF = input("Anything else would you like? y - for yes / n - for ready to checkout  : ")
                            if decisionF == "n":
                                if countF < 0:
                                    if decisionF not in menuF:
                                        break
                                    itemF.append(decisionF)
                                    print("")
                                else:
                                    print("")
                                    print("|=================================================================|")
                                    print("Quantity", countF, "Total price is $",totalF)#here its displayed the quantity of items and total price of items inputed by user
                                    print("|=================================================================|")
                                    print("")
                                    break
                        decisionD = ""
                        countD = 0
                        totalD = 0
                        while True:
                            itemD = input("enter ur drink: ")
                            if itemD in menuD:
                                totalD += menuD[itemD]
                                countD += 1
                            else:
                                print("Incorrect spelling, try select again 'optional'")
                            decisionD = input("Anything else would you like? y - for yes / n - for ready to checkout : ")
                            if decisionD == "n":
                                if countD < 0:
                                    if decisionD not in menuD:
                                        break
                                    itemD.append(decisionD)
                                    print("")
                                else:
                                    print("")
                                    print("|=================================================================|")
                                    print("Quantity", countD, "Total price is $",totalD)
                                    print("|=================================================================|")
                                    print("")
                                    print("")
                                    print("Quantity",(countF + countD), "Total price is $",(totalF + totalD))
                                    print("")
                                    break
                    else:
                        print("")
                        print("password wrong")#here is when user inputs wrong password and this will tell user password wrong same goes for the other 2
                        print("")
                        break
                else:
                    print("")
                    print("username wrong")#this one
                    print("")
                    break
            else:
                print("")
                print("create account first")#this one
                print("")
        
        elif choice == "E":
            break
        else:
            print("Invaild choice, please try again!!")


if __name__ == "__main__":
    main()
