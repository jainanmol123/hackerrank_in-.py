#!/bin/python3

import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    if(y1<y2 or (m1<m2 and y1<y2) or (m1<m2 and y1==y2)):
        return(0)
    elif y1==y2 and m1==m2:
        if d1<=d2:
            return(0)
        return((d1-d2)*15)
    elif y1==y2 and m1>m2:
        return(500*(m1-m2))
    else:
        return(10000)
        
        
    # Complete this function

if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
