from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def show_transaction(self):
        print("Transaction ID:", self.transaction_id)
        print("Amount:", self.__amount)

    @abstractmethod
    def make_payment(self):
        pass


class UPIPayment(Payment):
    def __init__(self, transaction_id, amount):
        super().__init__(transaction_id, amount)

    def make_payment(self):
        print("UPI Payment Successful")
        print("Paid Amount:", self.get_amount())


class CreditCardPayment(Payment):
    def __init__(self, transaction_id, amount):
        super().__init__(transaction_id, amount)

    def make_payment(self):
        print("Credit Card Payment Successful")
        print("Paid Amount:", self.get_amount())


class NetBankingPayment(Payment):
    def __init__(self, transaction_id, amount):
        super().__init__(transaction_id, amount)

    def make_payment(self):
        print("Net Banking Payment Successful")
        print("Paid Amount:", self.get_amount())


u = UPIPayment("TXN101", 500)
u.show_transaction()
u.make_payment()

print()

c = CreditCardPayment("TXN102", 1000)
c.show_transaction()
c.make_payment()

print()

n = NetBankingPayment("TXN103", 2000)
n.show_transaction()
n.make_payment()
