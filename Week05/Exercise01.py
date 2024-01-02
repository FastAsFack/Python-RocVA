course = 'the course price of python = $25'
laptop = 'the price of the laptop = €1200'

print(len(course))
print(course.capitalize())
print(course.title())
print(course.upper())
print(course.lower())
print(course.startswith('t'))
print(course.endswith('5'))
print(course.count("o"))
print(course.find("P"))
print(course.find('o'))
print(course.find('K'))
print(course.find('price'))
print(course.replace('price', 'amount'))
print(course.replace('$', '€'))
print("**************************************************")


'''
capitalize only capitalizes the first character of the string
title capitalizes the first letter of every word
'''

'''
the difference between startswith and endswith is that
it checks wether something starts with a certain character or ends with it
'''

'''
well lower converts everything to lower case and upper does the same but to uppercase 
'''

