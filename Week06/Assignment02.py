# Variables #
all_animals = []
# Code #
while True:
    userinput = input("Add an animal or 'exit (ex)': ")

    if userinput.lower() == "ex" or userinput.lower() == "exit":
        break

    all_animals.append(userinput)

if all_animals:
    print("The animal(s) is(are):", end=" ")
    for animal in all_animals[:-1]:
        print(userinput + ", ", end="")
    print(all_animals[-1])
else:
    print("No animals were added.")