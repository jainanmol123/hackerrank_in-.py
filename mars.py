#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count=0
    l=list(s)
    if l[0]=='S':
        count+=1	
    for i in range(1,len(l)):
         if i%3==1 and l[i]=='O':
             count+=1
        
         elif i%3==2 and l[i]=='S':
             count+=1
      
         elif i%3==0 and l[i]=='S':
             count+=1
         else:
             count+=0
     
    return(len(s)-count)

     
print(marsExploration('SOSSPSSQSSOR'))          


