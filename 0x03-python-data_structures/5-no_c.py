#!/usr/bin/python3

def no_c(my_string):
    output = my_string.translate({ord(x): None for x in 'cC'})
    return output
