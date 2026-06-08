basicSalary = float(input("Enter Basic Salary: "))
allowance = float(input("Enter Allowance: "))
deductions = float(input("Enter Deductions: "))

grossSalary = basicSalary + allowance
netSalary = grossSalary - deductions

print("Gross Salary =", grossSalary)
print("Deductions =", deductions)
print("Net Salary =", netSalary)
