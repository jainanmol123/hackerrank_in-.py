#!/bin/python3

import sys

def serviceLane(n, cases):
    for i in range(t):
        r=[]
        p=cases[i]
        for j in range(p[0],(p[1]+1)):
            r.append(width[j])
        print(min(r))
        
    # Complete this function

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = list(map(int, input().strip().split(' ')))
    cases = []
    for cases_i in range(t):
       cases_t = [int(cases_temp) for cases_temp in input().strip().split(' ')]
       cases.append(cases_t)
    result = serviceLane(n, cases)
    # print ("\n".join(map(str, result)))
