price = 8000
is_costumer = True
manufacture_year = 2010

if price >= 6000:
    price -= 200
elif is_costumer:
    price -= 250
elif manufacture_year < 2011:
    price -= 150
else:
    price -= 50

rounded_price = round(price, 2)

print(f"Total price is {rounded_price}")

'''
because it skips all the other discounts if the person is buying something
that's bigger then 6000
'''