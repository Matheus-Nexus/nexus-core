from .exceptions import BankError

class NexusBank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount: int):
        if amount <= 0:
            raise BankError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int):
        if amount <= 0:
            raise BankError("Amount must be positive")
        if amount > self.balance:
            raise BankError("Insufficient funds")
        self.balance -= amount
        return self.balance
