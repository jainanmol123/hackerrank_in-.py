#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    temp=[]
    for i in keyboards:
        for j in drives:
            if(i+j <=s):
                temp.append(i+j)
    temp.sort(reverse=True)
    if(len(temp)>0):
         return(temp[0])
    else:
         return(-1)
             
    # Complete this function

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
