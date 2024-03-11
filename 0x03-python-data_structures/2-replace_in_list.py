#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listLen = len(my_list)

    if(listLen != 0):
        if (idx < 0 or idx > listLen - 1):
            return my_list
        else:
            my_list[idx] = element
            return my_list
