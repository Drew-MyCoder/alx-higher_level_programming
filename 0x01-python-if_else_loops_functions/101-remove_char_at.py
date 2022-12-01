#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    j = 0
    for c in str:
        if j != n:
            new += c
        j += 1
    return new
