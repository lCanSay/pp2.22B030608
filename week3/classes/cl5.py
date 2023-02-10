class Account():
    def __init__ (self,owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if(self.balance < amount):
            print("Not enough money on balance")
        else:
            self.balance -= amount
        

a = Account("Andrew", 500)
a.withdraw(400)
print(a.balance)