#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of a data by another one  in a new list."""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
