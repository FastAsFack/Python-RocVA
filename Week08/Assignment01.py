def chooseSize(size):
    print("Choose your size T-Shirt")
    print("Small - $10  | Medium - $15  | Large - $20")

    size_input = input("Enter the size t-shirt you want: ").capitalize()

    size_msg = "You chose the size"
    if size_input in ["Small", "Medium", "Large"]:
        print(f"{size_msg}: {size_input}")
        if size_input == "Small":
            print(f"The price of {size_input} size T-Shirt is $10.")
        elif size_input == "Medium":
            print(f"The price of {size_input} size T-Shirt is $15.")
        elif size_input == "Large":
            print(f"The price of {size_input} size T-Shirt is $20.")
    else:
        print("Invalid size input. Please choose among Small, Medium, or Large.")

chooseSize("Any initial size")
