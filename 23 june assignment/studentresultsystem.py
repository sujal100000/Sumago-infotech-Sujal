from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, roll_no, student_name, marks):
        self.roll_no = roll_no
        self.student_name = student_name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def show_result(self):
        print("Roll Number:", self.roll_no)
        print("Student Name:", self.student_name)
        print("Marks:", self.__marks)

    @abstractmethod
    def calculate_percentage(self):
        pass


class ScienceStudent(Student):
    def __init__(self, roll_no, student_name, marks):
        super().__init__(roll_no, student_name, marks)

    def calculate_percentage(self):
        percentage = (self.get_marks() / 600) * 100
        print("Science Percentage:", percentage, "%")


class CommerceStudent(Student):
    def __init__(self, roll_no, student_name, marks):
        super().__init__(roll_no, student_name, marks)

    def calculate_percentage(self):
        percentage = (self.get_marks() / 500) * 100
        print("Commerce Percentage:", percentage, "%")


class ArtsStudent(Student):
    def __init__(self, roll_no, student_name, marks):
        super().__init__(roll_no, student_name, marks)

    def calculate_percentage(self):
        percentage = (self.get_marks() / 400) * 100
        print("Arts Percentage:", percentage, "%")


s = ScienceStudent(101, "Sujal", 540)
s.show_result()
s.calculate_percentage()

print()

c = CommerceStudent(102, "Rahul", 420)
c.show_result()
c.calculate_percentage()

print()

a = ArtsStudent(103, "Amit", 320)
a.show_result()
a.calculate_percentage()
