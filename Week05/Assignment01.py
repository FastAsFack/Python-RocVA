menu = "Hamburger, Pizza, Salad, Fish, Vegetables"

userinput = input("Enter your order to check it: ")

userinput = userinput.lower()
userinput = userinput.title()

if userinput in menu:
    print(f"{userinput} is on the menu")
else:
    print(f"{userinput} is added to the menu")
    menu += ", " + userinput
    print(f"The new menu is {menu}")

