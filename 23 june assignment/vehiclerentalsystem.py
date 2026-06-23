from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_no, rent_per_day):
        self.vehicle_no = vehicle_no
        self.__rent_per_day = rent_per_day

    def get_rent(self):
        return self.__rent_per_day

    def show_vehicle_details(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Rent Per Day:", self.__rent_per_day)

    @abstractmethod
    def calculate_rent(self, days):
        pass


class Bike(Vehicle):
    def __init__(self, vehicle_no, rent_per_day):
        super().__init__(vehicle_no, rent_per_day)

    def calculate_rent(self, days):
        total = self.get_rent() * days
        print("Bike Rent for", days, "days =", total)


class Car(Vehicle):
    def __init__(self, vehicle_no, rent_per_day):
        super().__init__(vehicle_no, rent_per_day)

    def calculate_rent(self, days):
        total = (self.get_rent() * days) + 500
        print("Car Rent for", days, "days =", total)


class Bus(Vehicle):
    def __init__(self, vehicle_no, rent_per_day):
        super().__init__(vehicle_no, rent_per_day)

    def calculate_rent(self, days):
        total = (self.get_rent() * days) + 1000
        print("Bus Rent for", days, "days =", total)


b = Bike("MH26AB1234", 500)
b.show_vehicle_details()
b.calculate_rent(3)

print()

c = Car("MH26CD5678", 1500)
c.show_vehicle_details()
c.calculate_rent(3)

print()

bs = Bus("MH26EF9999", 5000)
bs.show_vehicle_details()
bs.calculate_rent(3)
