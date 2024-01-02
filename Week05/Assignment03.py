# Recognized pet keywords
pets = ["dog", "cat", "rabbit"]

userinput = input("Enter some info about your pet: ").lower()  # Convert input to lowercase for case-insensitive comparison

# Check if any recognized pet keyword is present in the user input
if "dog" in userinput:
    print("Thanks for the info about your dog")
elif "cat" in userinput:
    print("Thanks for the info about your cat")
elif "rabbit" in userinput:
    print("Thanks for the info about your rabbit")
else:
    print("Sorry, the program cannot identify your pet.")
