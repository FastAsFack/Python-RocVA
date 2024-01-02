balance = 500
amount = int(input("Whats the amount you want to withdraw: "))


if(amount > 0):
    if(balance >= amount):
        newBalance = balance - amount
        print(f"Your new balance is: {newBalance}")
    else:
        print("Insufficient balance!")
        print(f"Your balance is {balance}")
else:
    print("You cannot withdraw (0) or negative amounts")

'''
if you change the amount to 400 it says that your new balance is 100
and if you change it to -30 it gives you the error
Of you cannot withdraw (0) or negative amounts
'''