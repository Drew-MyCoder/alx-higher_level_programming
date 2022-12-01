#!/usr/bin/python3
for num in range (0, 99):
    #print double number followed by a comma
    print("{:02d}, ".format(num)), end='\n' if num == 99)
