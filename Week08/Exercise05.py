def getNetSalary():
    taxrate = 0.35
    tax = 4300 * taxrate
    netSalary = 4300 - tax
    return netSalary

print(getNetSalary())

