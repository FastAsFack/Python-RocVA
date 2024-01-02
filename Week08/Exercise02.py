def countyFunction(country):
    print("You are from " + country)

    return input("Enter the name of your county: ")

user_input = input("Enter your country: ")
counrty = countyFunction(user_input)
print("Your county is:", counrty)
