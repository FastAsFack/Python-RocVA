student_count = 10

while student_count > 3:
    print(f"Student {student_count}!")
    student_count -= 1

print(f"Student Count: {student_count}")

'''
well now it removed 1 after each time it goes through the code
so for the 1st time it runs the code the count is 2 then its 1 and then its 0
it does the same if you change the student count to 10 but then 10 times till it hits 0
and if you change the while condition to > 3 it stops at 4 because it has 3 loops left then
which stands for 3 students
'''