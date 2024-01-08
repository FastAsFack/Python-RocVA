manufactures = ["Dell", "HP", "IBM", "Acer"]

position = input("Enter the index of brand: ")

try:
    position = int(position)
    print(f"The brand belongs to the index is: {manufactures[position]}")
except IndexError as ie:
    print("List index out of range")
except Exception as exc:
    print("Unexpected Error!")


