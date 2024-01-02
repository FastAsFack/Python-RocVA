var = input("Enter a variable value: ")
if var.isdigit():
    print("The Variable contains only numbers")
if var.islower():
    if var.isalpha():
        print("The variable contains only letters")
        print("The variable containers lowercase")
if var.isupper():
    if var.isalpha():
        print("The variable contains only uppercase")
        print("The variable containers lowercase")
if var.istitle():
    print("The variable is a title")
    print("The variable containers lowercase")