#!/usr/bin/python3
def to_upper(character):
    if ord(character) >= 97 and ord (character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)

    #string returned in upper case
def uppercase(string):
    new_string = ""
    for character in string:
        new_string += "%c" % to_upper(character)
    print("(:s)".format(new_string))
