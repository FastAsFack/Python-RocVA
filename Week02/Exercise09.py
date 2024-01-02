nr1 = ["Volvo", "Toyota"]
nr2 = ["Volvo", "Toyota"]
nr3 = nr1

print(nr1 is nr2)
print(nr1 is nr3)
print(nr1 == nr2)
print(nr1 is not nr2)

''''
yes because the variables nr1 and nr2 are exactly the same 
but because they use separate arrays its false

for the second print statement nr1 is nr3 so that's true
for the third print statement nr1 and nr2 are exactly the same
and because you used the is equal statement its true

for the fourth print statement because nr1 and nr2 are in separate arrays they're not the same
so it should also be true because you used a is not statement
'''