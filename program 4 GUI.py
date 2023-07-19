from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("program 4")#title of window

Loginfo = {}#Dictionary to store login info

#global variables
frame5_window = None  
chicken_sb = None
sncp_sb = None
sausageroll_sb = None
quiche_sb = None
tcnt_sb = None
pancakes_sb = None
Doughnut_sb = None
croissant_sb = None
latte_sb = None
coffee_sb = None
ic_sb = None
esp_sb = None
tea_sb = None
mt_sb = None
bt_sb = None
water_sb = None

#Adding a function to create the first frame whihc has the 3 three options and title/main page
def create_frame1():
    global frame1
    frame1 = Frame(root)
    frame1.grid()

    title = Label(frame1, text="Welcome to coffee cafe. Please choose the following options:")
    title.grid(row=0, column=0)

    btnCA = Button(frame1, text="Create account", command=frame2)
    btnCA.grid(row=1, column=0)

    btnL = Button(frame1, text="Login", command=frame3)
    btnL.grid(row=2, column=0)

    btnE = Button(frame1, text="Exit", command=exit)
    btnE.grid(row=3, column=0)

#Adding a second function to create the secound frame for creating account
def frame2():
    global frame2_window
    frame1.grid_forget()
    frame2_window = Frame(root)
    frame2_window.grid()

    title2 = Label(frame2_window, text="Please create your account")
    title2.grid(row=0, column=1)

    tuser = Label(frame2_window, text="Username:")
    tuser.grid(row=1, column=0)

    euser = Entry(frame2_window)
    euser.grid(row=1, column=1)

    tpass = Label(frame2_window, text="Password:")
    tpass.grid(row=3, column=0)

    epass = Entry(frame2_window)
    epass.grid(row=3, column=1)

    btnCA2 = Button(frame2_window, text="Submit", command=lambda: account(euser.get(), epass.get()))
    btnCA2.grid(row=4, column=1)

    back_btn = Button(frame2_window, text="Back", command=lambda: go_back(frame2_window))
    back_btn.grid(row=4, column=0)

#Adding function 3 to create the third frame for the login
def frame3():
    global frame3_window
    frame1.grid_forget()
    frame3_window = Frame(root)
    frame3_window.grid()

    title3 = Label(frame3_window, text="Please enter your login credentials")
    title3.grid(row=0, column=1)

    tuser2 = Label(frame3_window, text="Username:")
    tuser2.grid(row=1, column=0)

    euser2 = Entry(frame3_window)
    euser2.grid(row=1, column=1)

    tpass2 = Label(frame3_window, text="Password:")
    tpass2.grid(row=3, column=0)

    epass2 = Entry(frame3_window)
    epass2.grid(row=3, column=1)

    btnLogin = Button(frame3_window, text="Login", command=lambda: login(euser2.get(), epass2.get()))
    btnLogin.grid(row=4, column=1)

    back_btn = Button(frame3_window, text="Back", command=lambda: go_back(frame3_window))
    back_btn.grid(row=4, column=0)

#four function to handle the create account 
def account(euser, epass):
    Loginfo[euser] = epass #Adds user and pass to the loginfo dictionary
    messagebox.showinfo("Account created", "Account successfully made")#messagebox1
    frame2_window.grid_forget()
    create_frame1()

#fifth function to handle the login
def login(euser, epass):
    if euser in Loginfo and Loginfo[euser] == epass: #this line of code checks user and pass match the stored login info
        frame3_window.grid_forget()
        frame4()
        messagebox.showinfo("Login Correct", "Successfully logged in.")#messagebox1
    else:
        messagebox.showinfo("Login Failed", "Incorrect username or password. Please try again.")#messagebox3

def frame4():
    global frame4_window, chicken_sb, sncp_sb, sausageroll_sb, quiche_sb, tcnt_sb, pancakes_sb, Doughnut_sb, croissant_sb, latte_sb, coffee_sb, ic_sb, esp_sb, tea_sb, mt_sb, bt_sb, water_sb
    frame4_window = Frame(root)
    frame4_window.grid()

    cafe_name = Label(frame4_window, text="Hello welcome to coffee call cafe\nHeres our MENU")
    cafe_name.grid(row=0, column=1)

    food_label = Label(frame4_window, text="choose your breakfast:\n")
    food_label.grid(row=3, column=0)

    chicken_info = Label(frame4_window, text="Chicken Sandwich\n$10")
    chicken_info.grid(row=4, column=0)
    chicken_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    chicken_sb.grid(row=5, column=0)

    sncp_info = Label(frame4_window, text="Steak and cheese pie\n$9")
    sncp_info.grid(row=6, column=0)
    sncp_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    sncp_sb.grid(row=7, column=0)

    sausageroll_info = Label(frame4_window, text="Sausage Roll\n$6")
    sausageroll_info.grid(row=8, column=0)
    sausageroll_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    sausageroll_sb.grid(row=9, column=0)

    quiche_info = Label(frame4_window, text="Quiche\n$12")
    quiche_info.grid(row=10, column=0)
    quiche_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    quiche_sb.grid(row=11, column=0)

    tcnt_info = Label(frame4_window, text="Toasted cheese and tuna\n$15")
    tcnt_info.grid(row=12, column=0)
    tcnt_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    tcnt_sb.grid(row=13, column=0)

    pancakes_info = Label(frame4_window, text="Pancakes\n$5")
    pancakes_info.grid(row=14, column=0)
    pancakes_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    pancakes_sb.grid(row=15, column=0)

    Doughnut_info = Label(frame4_window, text="Doughnut\n$8")
    Doughnut_info.grid(row=16, column=0)
    Doughnut_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    Doughnut_sb.grid(row=17, column=0)

    croissant_info = Label(frame4_window, text="croissant\n$4")
    croissant_info.grid(row=18, column=0)
    croissant_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    croissant_sb.grid(row=19, column=0)

    drink_label = Label(frame4_window, text="choose your drink:\n")
    drink_label.grid(row=3, column=2)

    latte_info = Label(frame4_window, text="Latte\n$3")
    latte_info.grid(row=4, column=2)
    latte_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    latte_sb.grid(row=5, column=2)

    coffee_info = Label(frame4_window, text="Coffee\n$4")
    coffee_info.grid(row=6, column=2)
    coffee_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    coffee_sb.grid(row=7, column=2)

    ic_info = Label(frame4_window, text="Ice Coffee\n$8")
    ic_info.grid(row=8, column=2)
    ic_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    ic_sb.grid(row=9, column=2)

    esp_info = Label(frame4_window, text="Espresso\n$7")
    esp_info.grid(row=10, column=2)
    esp_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    esp_sb.grid(row=11, column=2)

    tea_info = Label(frame4_window, text="Tea\n$2")
    tea_info.grid(row=12, column=2)
    tea_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    tea_sb.grid(row=13, column=2)

    mt_info = Label(frame4_window, text="Milk Tea\n$4")
    mt_info.grid(row=14, column=2)
    mt_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    mt_sb.grid(row=15, column=2)

    bt_info = Label(frame4_window, text="Bubble tea\n$10")
    bt_info.grid(row=16, column=2)
    bt_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    bt_sb.grid(row=17, column=2)

    water_info = Label(frame4_window, text="Water\n$1")
    water_info.grid(row=18, column=2)
    water_sb = Spinbox(frame4_window, from_=0, to=10, width=5)
    water_sb.grid(row=19, column=2)

    finish = Button(frame4_window, text="checkout", command=frame5)
    finish.grid(row=20, column=1)
    
def frame5():
    global frame5_window
    frame4_window.grid_forget()
    frame5_window = Frame(root)
    frame5_window.grid()

    rt = Label(frame5_window, text="your checkout page\n")
    rt.grid(row=1, column=0)

    back_btn = Button(frame5_window, text="Go Back to menu", command=lambda: go_back(frame5_window))
    back_btn.grid(row=0, column=0)

    revealft_btn = Button(frame5_window, text="reveal your food: total price", command=lambda: button_clicked())
    revealft_btn.grid(row=1, column=0)

    revealdt_btn = Button(frame5_window, text="reveal your drink: total price", command=lambda: button_clicked2())
    revealdt_btn.grid(row=3, column=0)

    go_to_frame1_btn = Button(frame5_window, text="Return to home page", command=lambda: go_to_frame1(frame5_window))
    go_to_frame1_btn.grid(row=5, column=0) 

def go_to_frame1(frame):
    frame.grid_forget()
    create_frame1()

def go_back(frame):
    frame.grid_forget()
    if frame == frame5_window:
        frame4()
    else:
        create_frame1()

def button_clicked():
    global chicken_sb, sncp_sb, sausageroll_sb, quiche_sb, tcnt_sb, pancakes_sb, Doughnut_sb, croissant_sb
    
    chicken_total = int(chicken_sb.get()) * 10
    sncp_total = int(sncp_sb.get()) * 9
    sausageroll_total = int(sausageroll_sb.get()) * 6
    quiche_total = int(quiche_sb.get()) * 12
    tcnt_total = int(tcnt_sb.get()) * 15
    pancakes_total = int(pancakes_sb.get()) * 5
    Doughnut_total = int(Doughnut_sb.get()) * 8
    croissant_total = int(croissant_sb.get()) * 4
    
    total_priceF = chicken_total + sncp_total + sausageroll_total + quiche_total + tcnt_total + pancakes_total + Doughnut_total + croissant_total
    priceF = Label(frame5_window, text=f"Your total price: ${total_priceF}")
    priceF.grid(row=2, column=0)

def button_clicked2(): 
    global latte_sb, coffee_sb, ic_sb, esp_sb, tea_sb, mt_sb, bt_sb, water_sb

    latte_total = int(latte_sb.get()) * 3
    coffee_total = int(coffee_sb.get()) * 4
    ic_total = int(ic_sb.get()) * 8
    esp_total = int(esp_sb.get()) * 7
    tea_total = int(tea_sb.get()) * 2
    mt_total = int(mt_sb.get()) * 4
    bt_total = int(bt_sb.get()) * 10 
    water_total = int(water_sb.get()) * 1
    
    total_priceD = latte_total + coffee_total + ic_total + esp_total + tea_total + mt_total +  bt_total + water_total
    priceD = Label(frame5_window, text=f"Your total price: ${total_priceD}")
    priceD.grid(row=4, column=0)


#calling the main frame creation function
create_frame1()
root.mainloop()
