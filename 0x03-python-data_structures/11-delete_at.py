#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    #delete an item at a specific position in a list
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return(my_list)
