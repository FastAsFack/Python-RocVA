numbers = ["A", "B", "C", "D", "E"]
position = input("Enter a number: ")
try:
    position= int(position)
    print(numbers[position])
except IndexError as ie:
    print("Index Error")
except Exception as exc:
    print("Except")
