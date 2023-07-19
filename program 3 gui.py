from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("program 3") #title of window

Loginfo = {} #Dictionary to store login info

#Adding a function to create the first frame whihc has the 3 three options and title/main page
def create_frame1():
    global frame1
    frame1 = Frame(root)
    frame1.grid()

    title = Label(frame1, text="Welcome to coffee cafe. Please choose the following options:")#title of the first frame/app
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

# four function to handle the create account 
def account(euser, epass):
        Loginfo[euser] = epass # Adds user and pass to the loginfo dictionary
        messagebox.showinfo("Account created", "Account succesfully made")#messagebox1
        frame2_window.grid_forget()
        create_frame1()
        
# fifth function to handle the login
def login(euser, epass):
    if euser in Loginfo and Loginfo[euser] == epass: #this line of code checks user and pass match the stored login info
        messagebox.showinfo("Login Correct", "Succesfully logged in.")#messagebox2
    else:
        messagebox.showinfo("Login Failed", "Incorrect username or password. Please try again.")#messagebox3
        
#calling the main frame creation function
create_frame1()
root.mainloop()
