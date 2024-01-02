import random

userinput = input("Guess a number from 1 to 5: ")

# secret_number = random.randint(1,5)
#
# if secret_number == userinput:
#     print(f"You've chosen the correct answer")
# else:
#     print(f"You've chosen the incorrect answer the answer was {secret_number}")

secret_number = 4

if userinput == secret_number:
    print(f"Number 4 is correct")
else:
    print(f"Number {userinput} is incorrect the answer was {secret_number}")

# print(secret_number)

