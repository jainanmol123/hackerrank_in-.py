#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    s=[]
    for i in rating:
        if i>=90:
            s.append(i)
    p=sum(s)/len(s)
    t=round(p,2)
    print("{:.2f}".format(t))

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
