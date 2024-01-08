try:
    x = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    print(x/n)
except ZeroDivisionError:
    print("Exception: Cannot divide by zero")
else:
    print("Nothing went wrong")
