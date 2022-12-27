#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    numElem = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
            numElem += 1
        except IndedError:
            break

    print()
    return numElem
