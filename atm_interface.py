import sys
from datetime import datetime



class Atm:
    data = {}
    wid_lst = []
    dep_lst = []

    def __init__(self, PAN):
        if PAN in self.data:
            self.first_name = self.data[PAN][0]
            self.last_name = self.data[PAN][1]
            self.ID = PAN
            self.password = self.data[PAN][3]
            self.balance = self.data[PAN][4]
            vald = self.login()
            while not vald:
                vald = self.login()
            self.display()
        else:
            print("Looks like you do not have an account with us\n Would you like to have one :)\n y/n: ")
            ans = input()
            if ans == 'y' or ans == 'yes':
                self.reg_acc(PAN)
            else:
                sys.exit()

    def display(self):
        print('''Welcome! Please choose the desired operation from below:
				1-> Show Balance
				2-> Open Account
				3-> Withdraw Amount
				4-> Deposit Cash
				5-> Change PIN
                6-> Update Profile
                7-> Past Transaction
                8-> Mini Statement
                9-> Exit''')
        try:
            task = int(input())
            if task == 1:
                self.show_bal()
            elif task == 2:
                self.reg_acc(input('Enter PAN: '))
            elif task == 3:
                self.wid_cash(float(input('Enter amount to withdraw: ')))
            elif task == 4:
                self.dep_cash(float(input('Enter amount to deposit: ')))
            elif task == 5:
                self.pwd_reset()
            elif task == 6:
                self.update_info()
            elif task == 7:
                self.trans_hist()
            elif task == 8:
                self.mini_stat()
            else:
                print("Have a good day!")
                sys.exit()
        except ValueError:
            sys.exit()

    def show_bal(self):
        print("Your current account balance is: ", self.balance)
        print('\n')
        self.display()

    def reg_acc(self, PAN):
        if PAN not in self.data:
            info = ['', '', '', '', 0.00]
            self.first_name = input("Enter first name: ")
            self.last_name = input("Enter last name: ")
            self.ID = PAN
            self.password = input("Create a new PIN: ")
            self.balance = int(input('Deposit some amount at the counter: '))
            info[0] = self.first_name
            info[1] = self.last_name
            info[2] = self.ID
            info[3] = self.password
            info[4] = self.balance
            self.data[self.ID] = info
            print("Account created successfully!\nWelcome to the family", self.first_name, self.last_name)
            self.display()
        else:
            print("An account with this ID already exists in our database!.")
            self.display()

    def wid_cash(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
            self.display()
        if self.balance >= amount:
            print("withdrawal in progress...")
            self.balance -= amount
            print("withdrawal successful")
            self.wid_lst.append("withdrew  "+str(amount)+"        "+str(datetime.now()))
            self.display()

    def dep_cash(self, amount):
        self.balance += amount
        print("balance updated successfully")
        self.dep_lst.append("deposited  "+str(amount)+"      "+str(datetime.now()))
        self.display()

    def pwd_reset(self):
        old_pwd = input("Enter old PIN: ")
        if old_pwd == self.password:
            new_pwd = input("Enter new PIN: ")
            if new_pwd == old_pwd:
                print("New PIN can not be the old PIN. Try something else")
                self.pwd_reset()
            conf_pwd = input("Confirm new PIN: ")
            while new_pwd != conf_pwd:
                print("PIN did not match!\nTry Again")
                self.pwd_reset()
            print("PIN updated successfully")
            self.display()
        else:
            print("Incorrect PIN!\nTry Again")
            self.pwd_reset()

    def update_info(self):
        print('''1-> update first name
                2-> update last name
                3-> update ID''')
        ans = int(input())
        if ans == 1:
            self.data[self.ID][0] = input("Enter new first name: ")
        if ans == 2:
            self.data[self.ID][1] = input("Enter new last name: ")
        if ans == 3:
            self.data[self.ID][2] = input("Enter new ID: ")
        self.display()

    def trans_hist(self):
        for i in self.wid_lst:
            print(i)
        print()
        for i in self.dep_lst:
            print(i)
        self.display()

    def mini_stat(self):
        print("generating mini statement...")
        print("visit again!!!")
        self.display()

    def login(self):
        pwd = input('Enter your PIN: ')
        return pwd == self.password


Atm.data['0103EC191'] = ['Ujjawal', 'Kumar', '0103EC191', '123', 256.55]
# uks = Atm('0103EC191')
# usr = Atm('0157EC115')
