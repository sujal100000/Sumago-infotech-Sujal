from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, emp_name, basic_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.__basic_salary = basic_salary

    def get_salary(self):
        return self.__basic_salary

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Basic Salary:", self.__basic_salary)

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, emp_id, emp_name, basic_salary):
        super().__init__(emp_id, emp_name, basic_salary)

    def calculate_salary(self):
        bonus = self.get_salary() * 0.30
        total = self.get_salary() + bonus
        print("Bonus:", bonus)
        print("Total Salary:", total)


class Developer(Employee):
    def __init__(self, emp_id, emp_name, basic_salary):
        super().__init__(emp_id, emp_name, basic_salary)

    def calculate_salary(self):
        bonus = self.get_salary() * 0.20
        total = self.get_salary() + bonus
        print("Bonus:", bonus)
        print("Total Salary:", total)


class Intern(Employee):
    def __init__(self, emp_id, emp_name, basic_salary):
        super().__init__(emp_id, emp_name, basic_salary)

    def calculate_salary(self):
        bonus = self.get_salary() * 0.05
        total = self.get_salary() + bonus
        print("Bonus:", bonus)
        print("Total Salary:", total)


m = Manager(101, "Sujal", 50000)
m.show_details()
m.calculate_salary()

print()

d = Developer(102, "Rahul", 40000)
d.show_details()
d.calculate_salary()

print()

i = Intern(103, "Amit", 15000)
i.show_details()
i.calculate_salary()
