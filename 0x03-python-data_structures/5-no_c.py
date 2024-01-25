#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    new_string = my_string.lower()
    for char in new_string:
        if char != 'c':
            new_str += char
    return new_str
