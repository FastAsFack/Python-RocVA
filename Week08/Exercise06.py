def getNetSalary(grossSalary):
    taxrate = 0.30
    tax = grossSalary * taxrate
    netSalary = grossSalary - tax
    return netSalary

print(getNetSalary(4000))


