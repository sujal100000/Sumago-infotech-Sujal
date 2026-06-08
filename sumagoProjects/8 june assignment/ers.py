employee_id = input("Enter Employee ID: ")

employees = ["E101", "E102", "E103", "E104"]

if employee_id in employees:
    print("Employee Record Found")
else:
    print("Employee Record Not Found")