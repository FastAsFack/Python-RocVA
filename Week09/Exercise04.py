list = [3,1,6,9]

try:
    print(list[7])
except IndexError as ie:
    print(ie)
