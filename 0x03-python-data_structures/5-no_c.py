#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    strLen = len(my_list)
    i = 0

    while (i < strLen):
        if my_list[i] == 'c' or my_list[i] == 'C':
            my_list[i] = ""
        i = i + 1
    my_string = "".join(my_list)
    return my_string
