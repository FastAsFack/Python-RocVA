cars = ["Volvo", "Audi", "Toyota", "Honda", "BMW"]
cars2 = ["Kia", "Opel", "Nio"]

cars.extend(cars2)

cars.sort()
for car in cars:
    print(car, end=' ')
