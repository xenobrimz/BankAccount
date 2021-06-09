class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(f"Added ${amount} to your balance. Balance is now {self.balance}")
        return self
        
    def withdraw(self, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
            print(f"Withdrew ${amount} ")
            return self
        else:
            print("Insuficient Funds: deducting $5")
            self.balance -= 5
            return self
      
    def display_account_info(self):
        print(f"Your account balance is ${self.balance}")
        return self
        

    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance * self.int_rate
        return self

Act1 = BankAccount(0.5,100)
Act2 = BankAccount(0.5,100)

Act1.deposit(200).deposit(200).deposit(200).withdraw(400).yield_interest().display_account_info()
Act2.deposit(200).deposit(200).withdraw(400).withdraw(400).withdraw(400).withdraw(400).yield_interest().display_account_info()
    
