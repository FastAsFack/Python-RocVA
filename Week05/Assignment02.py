userinput = input("Enter a text: ")

if userinput.isupper():
    print(f"You entered uppercase")
    print(f"The first letter is either E or G.")
elif userinput.islower():
    print(f"You entered lowercase")
    print(f"The text doesn't start with E or G.")
elif userinput.startswith("E") or userinput.startswith("G"):
    print(f"The first letter is either E or G.")
else:
    print(f"The text doesn't start with E or G.")
