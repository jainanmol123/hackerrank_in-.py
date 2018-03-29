#!/bin/python3

import sys
import math

def encryption(s):
    p=[]
    l=len(s)
    t=math.sqrt(l)
    r=int(math.ceil(t))
    for x in range(r):
        temp=s[x::r]
        p.append(temp)
    return (' '.join(p))    
        
            
    
    # Complete this function

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
