import numpy
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a=numpy.array(a)    
print(numpy.prod(numpy.sum(a, axis = 0),axis=0))

