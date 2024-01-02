colors = ["yellow", "green", "red", "black", "white", "blue"]

userinput = input("Enter a color: ")

if userinput not in colors:
    print(f"{userinput} in colors is False")
else:
    print(f"{userinput} in colors is True")