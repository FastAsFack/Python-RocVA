x = 10
try:
    number = input("Enter a number: ")
    numberInt = int(number)
    print(x/numberInt)
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("Something went wrong")
