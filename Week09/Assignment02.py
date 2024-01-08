try:
    x = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    print(x/n)
except ZeroDivisionError:
    print("Cannot divide by zero")
    print("Show always this message")
except Exception as ie:
    print("Type Error")
    print("Show always this message")
else:
    print("Show always this message")


