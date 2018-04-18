#!/bin/python3

import sys

def migratoryBirds(n, ar):
    one=0
    two=0
    three=0
    four=0
    five=0
    count=[]
    for i in range(n):
        if ar[i]==1:
            one+=1
        elif ar[i]==2:
            two+=1
        elif ar[i]==3:
            three+=1
        elif ar[i]==4:
            four+=1
        else:
            five+=1
    count.append(one)
    count.append(two)
    count.append(three)
    count.append(four)
    count.append(five)
    t=max(count)
    return(count.index(t)+1)

    
            
            
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
