from abc import ABC, abstractmethod


class FoodOrder(ABC):
    def __init__(self, order_id, customer_name, food_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.__food_price = food_price

    def get_price(self):
        return self.__food_price

    @abstractmethod
    def generate_bill(self):
        pass

    def _restaurant_details(self):
        print("Restaurant: Food Express")

    def __apply_discount(self):
        return self.__food_price * 0.10

    def show_discount(self):
        print("Discount:", self.__apply_discount())


class VegOrder(FoodOrder):
    def __init__(self, order_id, customer_name, food_price):
        super().__init__(order_id, customer_name, food_price)

    def generate_bill(self):
        price = self.get_price()
        gst = price * 0.05
        total = price + gst

        self._restaurant_details()
        print("\nVeg Order Bill")
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Price:", price)
        print("GST (5%):", gst)
        print("Final Bill:", total)


class NonVegOrder(FoodOrder):
    def __init__(self, order_id, customer_name, food_price):
        super().__init__(order_id, customer_name, food_price)

    def generate_bill(self):
        price = self.get_price()
        gst = price * 0.10
        total = price + gst

        self._restaurant_details()
        print("\nNon-Veg Order Bill")
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Price:", price)
        print("GST (10%):", gst)
        print("Final Bill:", total)


v = VegOrder(101, "Sujal", 500)
v.generate_bill()
v.show_discount()

print()

n = NonVegOrder(102, "Rahul", 800)
n.generate_bill()
n.show_discount()
