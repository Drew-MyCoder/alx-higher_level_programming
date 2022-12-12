#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    list_key = list(a_dictionary.keys())

    for x in list_key:
        num += 1

    return (num)
