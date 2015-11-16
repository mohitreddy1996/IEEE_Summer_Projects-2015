k=2
def get_prime(n):
	p=[-1]*n
	global k
	for i in range(0,n):
		p[i]=k
		k=k+1
	for i in range(0,n):
		top=p[i]
		if p[i]!=0:
			for j in range(i+1,n):
				if p[j]%top==0:
					p[j]=0
	getprime=[-1]*(n+1)
	k=0
	for i in range(0,n):
		if p[i]!=0:
			getprime[k]=p[i]
			k+=1
	
	return getprime

num=int(raw_input("Enter the Number : "))
list1=get_prime(num)
for i in range(0,k):
	print list1[i]
