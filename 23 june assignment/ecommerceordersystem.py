from abc import ABC, abstractmethod


class Order(ABC):
    def __init__(self, order_id, product_name, product_price):
        self.order_id = order_id
        self.product_name = product_name
        self.__product_price = product_price

    def get_price(self):
        return self.__product_price

    def show_order_details(self):
        print("Order ID:", self.order_id)
        print("Product Name:", self.product_name)
        print("Product Price:", self.__product_price)

    @abstractmethod
    def calculate_total(self):
        pass


class LocalOrder(Order):
    def __init__(self, order_id, product_name, product_price):
        super().__init__(order_id, product_name, product_price)

    def calculate_total(self):
        shipping = 50
        total = self.get_price() + shipping
        print("Shipping Charge:", shipping)
        print("Total Amount:", total)


class StateOrder(Order):
    def __init__(self, order_id, product_name, product_price):
        super().__init__(order_id, product_name, product_price)

    def calculate_total(self):
        shipping = 150
        total = self.get_price() + shipping
        print("Shipping Charge:", shipping)
        print("Total Amount:", total)


class InternationalOrder(Order):
    def __init__(self, order_id, product_name, product_price):
        super().__init__(order_id, product_name, product_price)

    def calculate_total(self):
        shipping = 500
        total = self.get_price() + shipping
        print("Shipping Charge:", shipping)
        print("Total Amount:", total)


l = LocalOrder(101, "Headphones", 1000)
l.show_order_details()
l.calculate_total()

print()

s = StateOrder(102, "Smart Watch", 3000)
s.show_order_details()
s.calculate_total()

print()

i = InternationalOrder(103, "Laptop", 50000)
i.show_order_details()
i.calculate_total()
