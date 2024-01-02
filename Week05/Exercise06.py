secret_number = 7
userinput = input("Guess a number from 1 to 10: ")

if userinput.isdigit():
    userinput = int(userinput)

    if userinput >= 1 and userinput <= 10:
        if userinput == secret_number:
            print("Congratulations! You guessed the correct number.")
        elif userinput < secret_number:
            print("The number is higher than your guess.")
        else:
            print("The number is lower than your guess.")
    else:
        print("Please enter a number within the range of 1 to 10.")
else:
    print("Please enter only digits (numbers from 1 to 10).")
