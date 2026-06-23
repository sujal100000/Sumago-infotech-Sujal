from abc import ABC, abstractmethod


class Patient(ABC):
    def __init__(self, patient_id, patient_name, treatment_cost):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.__treatment_cost = treatment_cost

    def get_cost(self):
        return self.__treatment_cost

    def patient_details(self):
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.patient_name)
        print("Treatment Cost:", self.__treatment_cost)

    @abstractmethod
    def generate_bill(self):
        pass


class GeneralPatient(Patient):
    def __init__(self, patient_id, patient_name, treatment_cost):
        super().__init__(patient_id, patient_name, treatment_cost)

    def generate_bill(self):
        bill = self.get_cost() + (self.get_cost() * 0.10)
        print("General Patient Bill:", bill)


class ICUPatient(Patient):
    def __init__(self, patient_id, patient_name, treatment_cost):
        super().__init__(patient_id, patient_name, treatment_cost)

    def generate_bill(self):
        bill = self.get_cost() + (self.get_cost() * 0.25)
        print("ICU Patient Bill:", bill)


class EmergencyPatient(Patient):
    def __init__(self, patient_id, patient_name, treatment_cost):
        super().__init__(patient_id, patient_name, treatment_cost)

    def generate_bill(self):
        bill = self.get_cost() + (self.get_cost() * 0.40)
        print("Emergency Patient Bill:", bill)


g = GeneralPatient(101, "Sujal", 10000)
g.patient_details()
g.generate_bill()

print()

i = ICUPatient(102, "Rahul", 20000)
i.patient_details()
i.generate_bill()

print()

e = EmergencyPatient(103, "Amit", 15000)
e.patient_details()
e.generate_bill()
