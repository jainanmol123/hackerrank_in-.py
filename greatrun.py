for i in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	p=[]
	summ=0
	for i in range(n-k+1):
		for j in range(i,k):
			summ=summ+arr[j]
		p.append(summ)
		k=k+1
		summ=0
	print(max(p))
		# summ=0
# +
