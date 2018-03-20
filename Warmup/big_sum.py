import sys

def aVeryBigSum(n, ar):
    sum=0
    for i in ar:
        sum=sum+i
    return(sum)
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
