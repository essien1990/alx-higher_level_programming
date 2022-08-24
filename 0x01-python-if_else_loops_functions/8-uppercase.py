#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[n]) - number), end='')
    print()
