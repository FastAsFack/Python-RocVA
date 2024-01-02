userAge = float(input("Enter the age of the customer: "))
userPrice = float(input("Enter the price of the product: "))

if userAge >= 60:
    seniorDiscount = userPrice * 0.5
    finalPrice = userPrice - seniorDiscount
    print(f"The price of this customer is: €{finalPrice:.2f}")
elif userAge <= 10:
    youngDiscount = userPrice * 0.5
    finalPrice = userPrice - youngDiscount
    print(f"The price of this customer is: €{finalPrice:.2f}")
elif userAge >= 10:
    normalDiscount = userPrice * 0.10
    finalPrice = userPrice - normalDiscount
    print(f"The price of this customer is €{finalPrice:.2f}")