def calDiscount(amount, age):
    if age >= 50:
        amount = amount - (amount * (25 / 100))
        return amount
    else:
        amount = amount - (amount * (10 / 100))
        return amount

print(calDiscount(200, 49))  # Example usage
