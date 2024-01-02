price = 8000
is_customer = False
manufacture_year = 2010

if price >= 6000:
    price -= 200
if is_customer:
    price -= 250
if manufacture_year < 2011:
    price -= 150
else:
    price -= 10

rounded_price = round(price, 2)

print(f"Total price is {rounded_price}")