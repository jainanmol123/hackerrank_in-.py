import sys

def workbook(n, k, arr):
    j=1
    i=0
    m=1
    count=0
    while i<n:
        if m<=j and j<=min(m+k-1,arr[i]):
            count+=1
        m+=k
        j+=1
        
        if m>arr[i]:
            i+=1   #next chapter
            m=1
    return count        
        
    # Complete this function

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)
