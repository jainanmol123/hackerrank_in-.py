#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=1
    current_pos=0
    while(i<len(c)-1):
        if not c[i+1]==1:
            current_pos=current_pos+1
            i=i+2
        else:
            current_pos=current_pos+1
            i=i+1
    if i==n-1:
        return current_pos+1
    return current_pos
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

