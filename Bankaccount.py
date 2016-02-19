class BankAccount:
    count = 0
    """ Class definition modeling the behavior of a simple bank account """
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        #return self.initial_balance
    def deposit(self, amount):
        """Deposits the amount into the account."""
        #self.deposit = amount 
        self.initial_balance = self.initial_balance + amount
        #return self.initial_balance
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        #self.withdraw = amount
        #balance = self.initial_balance
        self.initial_balance = self.initial_balance - amount
        if self.initial_balance < 0:
            self.initial_balance = self.initial_balance - 5
            BankAccount.count += 1
        #return self.initial_balance
        #self.initial_balance = self.initial_balance - amount
    def get_balance(self):
        """Returns the current balance in the account."""
        self.get_balance = self.initial_balance 
        return self.get_balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        #count = 0
        return BankAccount.count*5
        
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()