var = input("Enter the weather (Sunny, Rainy, Snowy): ")

if var.isupper():
    print("You've selected SUNNY -- Wear a t-shirt")
if var.islower():
    print("You've selected rainy -- You need an umbrella")
for letter in var:
    if letter.isupper():
        print("You've selected sNOwy -- You need a warm coat")