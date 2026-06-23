from abc import ABC, abstractmethod


class Ticket(ABC):
    def __init__(self, booking_id, customer_name, base_price):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.__base_price = base_price

    def get_price(self):
        return self.__base_price

    def show_booking_details(self):
        print("Booking ID:", self.booking_id)
        print("Customer Name:", self.customer_name)
        print("Base Price:", self.__base_price)

    @abstractmethod
    def ticket_price(self):
        pass


class SilverTicket(Ticket):
    def __init__(self, booking_id, customer_name, base_price):
        super().__init__(booking_id, customer_name, base_price)

    def ticket_price(self):
        total = self.get_price() + 50
        print("Silver Ticket Price:", total)


class GoldTicket(Ticket):
    def __init__(self, booking_id, customer_name, base_price):
        super().__init__(booking_id, customer_name, base_price)

    def ticket_price(self):
        total = self.get_price() + 100
        print("Gold Ticket Price:", total)


class PlatinumTicket(Ticket):
    def __init__(self, booking_id, customer_name, base_price):
        super().__init__(booking_id, customer_name, base_price)

    def ticket_price(self):
        total = self.get_price() + 200
        print("Platinum Ticket Price:", total)


s = SilverTicket(101, "Sujal", 300)
s.show_booking_details()
s.ticket_price()

print()

g = GoldTicket(102, "Rahul", 300)
g.show_booking_details()
g.ticket_price()

print()

p = PlatinumTicket(103, "Amit", 300)
p.show_booking_details()
p.ticket_price()
