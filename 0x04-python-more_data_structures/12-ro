#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string or type(roman_string) != str):
        return None
    else:
        myHash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
        integer = 0
        for i in range(len(roman_string)):
            if i+1 < len(roman_string) and myHash[roman_string[i]] < myHash[roman_string[i+1]]:
                integer -= myHash[roman_string[i]]
            else:
                integer += myHash[roman_string[i]]
        return integer
