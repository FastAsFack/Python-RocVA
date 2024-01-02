playerName = input("Enter the player's name: ")
playerAge = float(input(f"Enter the age of {playerName}: "))
playerLength = float(input(f"Enter the height of {playerName} (in centimeters): "))

if playerAge >= 16 and playerAge <= 34 and playerLength >= 180:
    print(f"{playerName} is Accepted!")
else:
    print(f"{playerName} is Rejected.")

