import sys

def bonAppetit(n, k, b, ar):
    p=sum(ar)-ar[k]
    if p/2==b:
        return('Bon Appetit')
    else:
        return((b-int(p/2)))
    
    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
