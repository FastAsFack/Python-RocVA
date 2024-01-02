while True:
    price = float(input("Enter a price lower than $20: "))
    if price < 20:
        print(f"The price you entered is ${price:.2f}")
        break
    else:
        print("Please enter a price lower than $20.")
