from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, acc_no, holder_name, balance):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, acc_no, holder_name, balance):
        super().__init__(acc_no, holder_name, balance)

    def calculate_interest(self):
        interest = self.get_balance() * 0.04
        print("Savings Interest:", interest)


class CurrentAccount(Account):
    def __init__(self, acc_no, holder_name, balance):
        super().__init__(acc_no, holder_name, balance)

    def calculate_interest(self):
        interest = self.get_balance() * 0.02
        print("Current Account Interest:", interest)


class FixedDepositAccount(Account):
    def __init__(self, acc_no, holder_name, balance):
        super().__init__(acc_no, holder_name, balance)

    def calculate_interest(self):
        interest = self.get_balance() * 0.08
        print("Fixed Deposit Interest:", interest)


s = SavingsAccount(101, "Sujal", 10000)
s.deposit(2000)
s.withdraw(1000)
print("Balance:", s.get_balance())
s.calculate_interest()

print()

c = CurrentAccount(102, "Rahul", 15000)
c.deposit(5000)
print("Balance:", c.get_balance())
c.calculate_interest()

print()

f = FixedDepositAccount(103, "Amit", 50000)
print("Balance:", f.get_balance())
f.calculate_interest()
