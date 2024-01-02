userinput = int(input("Enter an amount: "))
print(f"${userinput}", end=", ")

for i in range(4):
    userinput += 1
    print(f"${userinput}", end=", ")

