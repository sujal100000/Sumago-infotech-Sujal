percentage = float(input("Enter your percentage: "))
family_income = float(input("Enter annual family income: "))

if percentage >= 75 and family_income <= 300000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")