#!/usr/bin/python3
def element_at(my_list, idx):
    listLen = len(my_list)

    if(listLen != 0):
        if (idx < 0 or idx > listLen - 1):
            return None
        else:
            return my_list[idx]
