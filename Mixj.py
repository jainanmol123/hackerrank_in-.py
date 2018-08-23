t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	p=list(map(int,input().split()))
	count=0
	for i in range(len(p)):
		if i%2==0:
			count+=p[i]
		else:
			count-=p[i]
	
	if k<=count:
		print(1)
	else:
		print(2)
