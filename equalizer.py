import sys

def equalizeArray(arr):
    co=0
    p=max(arr,key=arr.count)
    for i in arr:
        if i==p:
            co+=1
    return(len(arr)-co)        
    
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
