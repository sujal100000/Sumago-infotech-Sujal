from abc import ABC, abstractmethod


class Subscription(ABC):
    def __init__(self, user_name, monthly_fee):
        self.user_name = user_name
        self.__monthly_fee = monthly_fee

    def get_fee(self):
        return self.__monthly_fee

    def show_plan_details(self):
        print("User Name:", self.user_name)
        print("Monthly Fee:", self.__monthly_fee)

    @abstractmethod
    def show_features(self):
        pass


class BasicPlan(Subscription):
    def __init__(self, user_name, monthly_fee):
        super().__init__(user_name, monthly_fee)

    def show_features(self):
        print("Basic Plan Features")
        print("1 Screen")
        print("SD Quality")


class StandardPlan(Subscription):
    def __init__(self, user_name, monthly_fee):
        super().__init__(user_name, monthly_fee)

    def show_features(self):
        print("Standard Plan Features")
        print("2 Screens")
        print("HD Quality")


class PremiumPlan(Subscription):
    def __init__(self, user_name, monthly_fee):
        super().__init__(user_name, monthly_fee)

    def show_features(self):
        print("Premium Plan Features")
        print("4 Screens")
        print("Ultra HD Quality")


b = BasicPlan("Sujal", 199)
b.show_plan_details()
b.show_features()

print()

s = StandardPlan("Rahul", 499)
s.show_plan_details()
s.show_features()

print()

p = PremiumPlan("Amit", 799)
p.show_plan_details()
p.show_features()
