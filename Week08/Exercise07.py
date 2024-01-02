def getNetSalary(grossSalary, taxRate):
    tax = grossSalary * taxRate
    netSalary = grossSalary - tax
    return netSalary

print(getNetSalary(6120, 0.40))