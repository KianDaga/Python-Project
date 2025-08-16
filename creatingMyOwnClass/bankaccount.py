class BankAccount:

    def __init__(self, id,  balance, company, name):
        self.id = id
        self.company = company
        self.balance = balance
        self.name = name

    def withdraw(self, amount):
        if self.balance < amount : 
            print(f"Insuficcient Funds, balance is {self.balance}")
        else: 
            self.balance -= amount
            print(f"You have withdrawn {amount}. Account balance is {self.balance}")

    def deposit(self,amount): 
        self.balance += amount 
        print(f"You have deposited {amount}, Your balance is now {self.balance}")       

    
    def checkbalance(self):
        print(f"Your Balance is: {self.balance}")   

    def transfer(self, amount, BankAcc):
        if  self.balance >= amount:
            self.balance = self.balance - amount
            BankAcc.balance = BankAcc.balance + amount
            print(f"Succesfully Transfered! {amount} Your new balance is: {self.balance}")
        else:
            print("Transfer Failed, funds unavailable! For more information, visit https://www.idiot.org")    

          
               
    


my_account = BankAccount(id="12345", balance=300, company="OCBC", name="my_account")
my_2nd_account = BankAccount(id="23451", balance=500, company="DBS", name="my_2nd_account")
print(my_account.id)
print(my_account.balance)
print(my_account.company)
my_account.deposit(500)
my_account.checkbalance
my_account.transfer(900, my_2nd_account)

