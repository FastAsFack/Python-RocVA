try:
    nr = int(input("Enter a number between 1 and 100: "))
    if nr < 1 or nr > 100:
        raise ValueError("The number is out of range")
    else:
        print("The number", nr, "is accepted")
except ValueError as ve:
    print(1, ve)
