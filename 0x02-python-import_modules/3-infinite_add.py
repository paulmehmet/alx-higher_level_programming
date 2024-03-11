#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    argvLen = len(argv)
    i = 0
    res = 0
    if argvLen != 0:
        while i < argvLen:
            res = res + int(argv[i])
            i = i + 1
        print("{:d}".format(res), end="\n")
    else:
        print("{:d}".format(0), end="\n")
