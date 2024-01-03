x = 10
number = input("Enter a number: ")

try:
    intNumber = int(number)
    print(x / intNumber)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception:
    print("Something went wrong!")
finally:
    print("Finally block is always executed!!")

