#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    count=0
    ar.sort()
    for i in ar:
        if(i==ar[-1]):
            count=count+1
    return(count)      
            
    
