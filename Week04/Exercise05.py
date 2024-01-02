is_certified = True
years_experience = 3

if is_certified and years_experience == 4:
    print("Salary is €4000")
elif is_certified and years_experience == 5:
    print("Salary is €4500")
elif is_certified and years_experience >= 6:
    print("Salary is 5000")
elif is_certified and years_experience >= 7:
    print("Salary is 5500")
elif is_certified and years_experience >= 8:
    print("Salary is 6000")
else:
    print("Sorry, Rejected")

'''
the salary for people with 8 years experience you get €6000
but the expected salary is about 4000
'''