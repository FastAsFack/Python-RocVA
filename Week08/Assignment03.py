def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = 25
num2 = 50
num3 = 30

largest_number = find_largest_number(num1, num2, num3)
print(f"The sequence of numbers is {num1}, {num2}, {num3}")
print(f"The largest number is {largest_number}")
