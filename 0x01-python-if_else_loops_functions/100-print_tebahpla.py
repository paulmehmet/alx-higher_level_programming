#!/usr/bin/python3
j = 0
for i in range(122, 96, -1):
    if (j % 2 != 0):
        i = i - 32
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i), end="")
    j = j + 1
