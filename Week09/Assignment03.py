
try:
    num1 = int(input("Enter the 1st positive number: "))
    num2 = int(input("Enter the 2nd positive number: "))

    if num1 < 0 or num2 < 0:
        raise ValueError("Please enter positive numbers only.")

    result = num1 * num2
    print(f"{num1} x {num2} = {result}")

except ValueError as ve:
    print(f"ValueError: {ve}")



