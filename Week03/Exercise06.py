course = 'the course price of python = $25'

print('Python' in course)
'''
this should return false because a string is always in lowercase so Python is not in the course variable
'''

print('python' in course)
'''
This should return true because the string is always in lowercase so its in the variable
'''
print('$' in course)
'''
this should return true because the dollar sign is in the course variable
'''
print('€' not in course)
'''
this should return true because we used a not in membership operator
and that should return true if it doesnt match any thing
from the string inside of the variable
'''