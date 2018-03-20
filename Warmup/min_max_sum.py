import sys

def miniMaxSum(arr):
    sum=0
    srr=[]
    for i in arr:
        sum=sum+i
    for j in arr:
        srr.append(sum-j)
    srr.sort()
    print(srr[0],srr[-1])
    
    # Complete this function

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
