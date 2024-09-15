"""
Liskov Substitution Principle: The Liskov Substitution Principle states that objects of a superclass should be 
replaceable with objects of its subclasses without affecting the correctness of the program. 
In other words, a subclass should override the methods of the superclass in such a way that 
the behavior of the subclass remains consistent with the behavior of the superclass.
"""

# Violation of the Liskov Substitution Principle
class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

class SavingsAccount(BankAccount):
    def withdraw(self, amount: float):
        if self.balance >= amount + 10:
            self.balance -= amount + 10
        else:
            print("Insufficient balance")

def make_withdrawal(account: BankAccount, amount: float):
    account.withdraw(amount)

if __name__ == "__main__":
    bank_account = BankAccount(100)
    make_withdrawal(bank_account, 50)
    print(bank_account.balance)
    
    savings_account = SavingsAccount(100)
    # Violation of the Liskov Substitution Principle - The behavior of the subclass SavingsAccount is not 
    # consistent with the behavior of the superclass BankAccount, as the withdraw() method of the subclass
    # deducts an additional fee of $10.
    make_withdrawal(savings_account, 50)
    print(savings_account.balance)

### Adhering to the Liskov Substitution Principle
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: float) -> None:
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount: float):
        if self.balance >= amount + 10:
            self.balance -= amount + 10
        else:
            print("Insufficient balance")

class CurrentAccount(BankAccount):
    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

def make_withdrawal(account: BankAccount, amount: float):
    account.withdraw(amount)

if __name__ == "__main__":
    bank_account = CurrentAccount(100)
    make_withdrawal(bank_account, 50)
    print(bank_account.balance)
    
    savings_account = SavingsAccount(100)
    make_withdrawal(savings_account, 50) # This will work as expected, it's overriding the abstract withdraw method
    print(savings_account.balance)
    