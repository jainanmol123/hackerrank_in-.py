#!/bin/python3

import sys

def taumBday(b, w, x, y, z):
    if x<y:
        if x+z>y:
            return(x*b+y*w)
        elif x+z<y:
            return(x*b+w*(x+z))
    if x>y:
        if y+z>x:
            return(x*b+y*w)
        elif y+z<x:
            return(b*(y+z)+w*y)
    if x==y:
        return(x*b+y*w)
    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print(result)
