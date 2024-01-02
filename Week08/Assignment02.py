def calculate_gold_ounces(amount):
    gold_price_per_ounce = 1900.00
    ounces_of_gold = amount / gold_price_per_ounce
    return ounces_of_gold

amount_in_dollars = float(input("Enter the amount in dollars: "))
gold_amount = calculate_gold_ounces(amount_in_dollars)
print(f"With ${amount_in_dollars:.2f}, you can buy {gold_amount:.2f} ounces of gold.")


