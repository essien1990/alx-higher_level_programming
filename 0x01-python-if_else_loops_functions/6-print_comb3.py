#!/usr/bin/python3
for number in range(0,90):
    if number / 10 < num % 10:
        if number != 89:
            print('{:02d}'.format(number), end=", ")
        else:
            print('{:02d}'.format(num+1))
