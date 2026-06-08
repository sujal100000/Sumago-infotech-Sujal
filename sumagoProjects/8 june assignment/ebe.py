salary = float(input("Enter employee salary: "))
years = int(input("Enter years of job: "))

if years >= 5:
    bonus = salary * 0.10
    print("Eligible for Bonus")
    print("Bonus Amount =", bonus)
else:
    print("Not Eligible for Bonus")
