'''
Converting dollar amounts to euro

dollar = 0.95 euro

Ask the user to enter an amount in dollars
Convert the dollar amount to euros and print it.
Round the amount to 2 decimals.

'''


dollar = 0.95

userinput = input("Enter an amount in dollars: ")

currencyconvert = float(userinput) * 0.95

roundedcurrency = round(currencyconvert, 2)

print(f"The amount of ${userinput} is {roundedcurrency}")
