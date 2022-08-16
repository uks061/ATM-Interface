from tkinter import *
from tkinter.ttk import *

welcome_win = Tk()

bg = PhotoImage(file="pictures/Uks1.png")
canvas = Canvas(welcome_win, width=100, height=100)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

usr = {"0103EC191191":["Ujjawal", "Kumar", "0103EC191191", 123, 256.66]}

def dis_win(event):
    global dis
    dis = Toplevel()
    dis_but = Button(master=dis, text="DISPLAY", width=8)
    dis_but.pack()
    dis_but.bind("<Button-1>", display)
    dis.deiconify()

def display(event):
    print('Welcome! Please choose the desired operation from below:')

def login(event):
    pwd = int(input('Enter your PIN: '))
    for i in usr.values():
        if i[3] == pwd:
            welcome_win.withdraw()
            dis_win(event)
        else:
            print("Please enter your correct pin.\nIf you don't have an account with us, click SIGNUP to register")
            # welcome_win.deiconify()


def signup(event):
    try:
        PAN = input("Please Enter Your PAN:")
        if PAN not in usr:
            info = ['', '', '', '', 0.00]
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            ID = PAN
            password = input("Create a new PIN: ")
            balance = int(input('Deposit some amount at the counter: '))
            info[0] = first_name
            info[1] = last_name
            info[2] = ID
            info[3] = password
            info[4] = balance
            usr[PAN] = info
            print("Account created successfully!\nWelcome to the family", first_name, last_name)
            welcome_win.withdraw()
            dis_win(event)

        else:
            print("An account with this ID already exists in our database!.\nPlease LOGIN to continue")
            # welcome_win.deiconify()

    except:
        print("Unfortunately something went wrong!! Please try again")

login_but = Button(master=welcome_win, text="LOGIN")#, height=10)#, width=10)
login_but.pack()
login_but.bind("<Button-1>", login)

sign_but = Button(master=welcome_win, text="SIGNUP")#, height=10)#, width=10)
sign_but.pack()
sign_but.bind("<Button-1>", signup)


welcome_win.mainloop()

